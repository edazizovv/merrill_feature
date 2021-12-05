#


#
import pandas


#


#
def standard_treat(data, no, diff, b100, b100diff, pct):
    data__pct = data[pct].pct_change(fill_method=None)
    data__no = data[no]
    data__diff = data[diff].diff()
    data__by_100_diff = (data[b100diff] / 100).diff()
    data__by_100 = data[b100] / 100
    data_res = pandas.concat((data__pct,
                              data__no,
                              data__diff,
                              data__by_100_diff,
                              data__by_100), axis=1)
    return data_res


def lag(data, n_lags):
    data_lagged = data.copy()
    for j in range(n_lags):
        data_lagged[[x + '_LAG{0}'.format(j + 1) for x in data.columns.values]] = data.shift(periods=(j + 1))
    return data_lagged


def wise_drop(data, nan_depth):
    wise = []
    for j in range(nan_depth):
        for c in data.columns.values:
            if pandas.isna(data[c].values[-(j + 1)]):
                wise.append('{0}_LAG{1}'.format(c, j + 1))
    return wise


def add_by_substring(columns, substrings, add_to):
    return [c for c in columns if any([d in c for d in substrings])] + add_to

