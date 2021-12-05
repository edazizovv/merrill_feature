
# mm = granger
# a = pandas.DataFrame(X_train.numpy()).corr(method=mm)
# b = cut_btw__pair(X_train.numpy(), method=mm, thresh=0.5)
# b = cut_fwd__pair(X_train.numpy(), Y_train.numpy(), method=mm, thresh=0.5)
# c = pandas.DataFrame(X_train.numpy()[:, b]).corr(method=mm)

# x = X_train[:, [0, 1]].numpy()

# cc = Correlated(model=LinearRegression, kwargs={})
# pearson(x=x[:, 0], y=x[:, 1])
# cc.corr(x=x[:, 0], y=x[:, 1])
# granger(x=x[:, 0], y=x[:, 1])
# mutual(x=x[:, 0], y=x[:, 1])
# ks(x=x[:, 0], y=x[:, 1])
# kl(x=x[:, 0], y=x[:, 1])
# cross(x=x[:, 0], y=x[:, 1])

# threshes = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
# transes = [pearson, cross, ks, mutual]
# transes = [pearson, cross, ks, mutual, granger]
# threshes = [1.0]
# transes = [pearson]
