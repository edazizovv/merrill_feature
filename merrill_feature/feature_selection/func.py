#


#
import numpy
from scipy import stats

from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import mutual_info_regression


#


#
def pearson(x, y):
    p, _ = stats.pearsonr(x, y)
    return p


class Correlated:

    def __init__(self, model, kwargs):
        self.model = model
        self.kwargs = kwargs

    def corr(self, x, y):
        model = self.model(**self.kwargs)
        model.fit(X=x.reshape(-1, 1), y=y)
        y_hat = model.predict(X=x.reshape(-1, 1))
        return pearson(x=y_hat, y=y)


def granger(x, y, n_lags=4):
    recorded = []

    X, Y = [], []

    for j in range(n_lags):
        X.append(x[j:-n_lags + j].reshape(-1, 1))
        Y.append(y[j:-n_lags + j].reshape(-1, 1))

    y_ = y[n_lags:]

    done = False
    x_mask = [True] * n_lags
    x_codes = numpy.array(list(range(n_lags)))
    y_mask = [True] * n_lags
    y_codes = numpy.array(list(range(n_lags)))

    while not done:

        # build an ols model

        Z = numpy.concatenate(X + Y, axis=1)[:, x_mask + y_mask]

        model = LinearRegression()
        model.fit(X=Z, y=y_)

        params = numpy.append(model.intercept_, model.coef_)
        predictions = model.predict(Z)

        # t-testing

        Z_extended = numpy.append(numpy.ones(shape=(Z.shape[0], 1)), Z, axis=1)
        mse = ((y_ - predictions) ** 2).sum() / (Z_extended.shape[0] - Z_extended.shape[1])

        params_variance = mse * (numpy.linalg.inv(numpy.dot(Z_extended.T, Z_extended)).diagonal())
        params_std = numpy.sqrt(params_variance)
        params_standardized = params / params_std

        t_test_p_values = [2 * (1 - stats.t.cdf(numpy.abs(ps), (Z_extended.shape[0] - Z_extended.shape[1])))
                           for ps in params_standardized]

        # f-testing

        r_squared = model.score(X=Z, y=y_)

        n = Z.shape[0]
        k = Z.shape[1] + 1

        f_statistic_value = (r_squared / (1 - r_squared)) * ((n - k - 1) / k)

        f_test_p_values = 1 - stats.f(k - 1, n - k).cdf(f_statistic_value)

        recorded.append(numpy.min([f_test_p_values] + t_test_p_values))

        t_test_p_values_max = numpy.array(t_test_p_values).argmax()

        if t_test_p_values_max < numpy.array(x_mask).sum():
            x_mask[x_codes[x_mask][t_test_p_values_max]] = False
        else:
            y_mask[y_codes[y_mask][t_test_p_values_max - numpy.array(x_mask).sum()]] = False

        if numpy.array(x_mask).sum() == 0:
            done = True

    min_result = 1 - numpy.min(recorded)

    return min_result


def mutual(x, y):
    m = mutual_info_regression(X=x.reshape(-1, 1), y=y)[0]
    return m


def ks(x, y):
    s, _ = stats.ks_2samp(data1=x, data2=y)
    return 1 - s


def kl(x, y):
    x_, _ = numpy.histogram(x, density=True)
    y_, _ = numpy.histogram(y, density=True)
    l = stats.entropy(pk=x_, qk=y_)
    return 1 - l


def cross(x, y):
    o = numpy.correlate(a=x, v=y)[0]
    return o
