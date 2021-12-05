#


#
import numpy


#


#
def up(x_train, y_train, x_test, y_test, model, model_kwg, on):

    done = False

    yield_on_train__best = 0
    var_on_train__best = -1

    mask = [False] * x_train.shape[1]
    codes = numpy.array(numpy.arange(x_train.shape[1]))

    while not done:

        improved_ix = []
        improved_value = []

        for i in range(len(mask)):

            if not mask[i]:

                yield_on_train__average = []
                var_on_train__average = []

                mask_copy = [x for x in mask]
                mask_copy[i] = True

                for _ in range(10):

                    still = model(**model_kwg)
                    still.still(x_train[:, codes[mask_copy]], y_train, x_test, y_test)
                    summary = still.plot(X_train=x_train, Y_train=y_train, X_test=x_test, Y_test=y_test, on='filt', do_plot=False)

                    yield_on_train = summary[0].values[0, 0]
                    var_on_train = summary[0].values[0, 3]

                    yield_on_train__average.append(yield_on_train)
                    var_on_train__average.append(var_on_train)

                yield_on_train__average = numpy.mean(yield_on_train__average)
                var_on_train__average = numpy.mean(var_on_train__average)

                yield_criteria = yield_on_train__average > yield_on_train__best
                var_criteria = var_on_train__average < var_on_train__best

                if on == 'yor':
                    if yield_criteria:
                        improved_ix.append(i)
                        improved_value.append(yield_on_train__average)
                elif on == 'vor':
                    if var_criteria:
                        improved_ix.append(i)
                        improved_value.append(var_on_train__average)
                else:
                    raise Exception("Feature Selection Iterative: Up: Invalid target specification - should be valued"
                                    "as either 'yor' or 'vor'")

        improved_ix = numpy.array(improved_ix)
        improved_value = numpy.array(improved_value)

        if len(improved_ix) == 0:
            done = True

        if on == 'yor' or on == 'vor':
            max_ix = improved_value.argmax()
        else:
            raise Exception("Feature Selection Iterative: Up: Invalid target specification - should be valued"
                            "as either 'yor' or 'vor'")

        mask[max_ix] = True

        if all(mask):
            done = True

    return mask


def down(x_train, y_train, x_test, y_test, model, m_kwg, on):

    done = False

    yield_on_train__best = 0
    var_on_train__best = -1

    mask = [True] * x_train.shape[1]
    codes = numpy.array(numpy.arange(x_train.shape[1]))

    while not done:

        improved_ix = []
        improved_value = []

        for i in range(len(mask)):

            if mask[i]:

                yield_on_train__average = []
                var_on_train__average = []

                mask_copy = [x for x in mask]
                mask_copy[i] = False

                for _ in range(10):

                    still = model(**m_kwg)
                    still.still(x_train[:, codes[mask_copy]], y_train, x_test, y_test)
                    summary = still.plot(X_train=x_train, Y_train=y_train, X_test=x_test, Y_test=y_test, on='filt', do_plot=False)

                    yield_on_train = summary[0].values[0, 0]
                    var_on_train = summary[0].values[0, 3]

                    yield_on_train__average.append(yield_on_train)
                    var_on_train__average.append(var_on_train)

                yield_on_train__average = numpy.mean(yield_on_train__average)
                var_on_train__average = numpy.mean(var_on_train__average)

                yield_criteria = yield_on_train__average > yield_on_train__best
                var_criteria = var_on_train__average < var_on_train__best

                if on == 'yor':
                    if yield_criteria:
                        improved_ix.append(i)
                        improved_value.append(yield_on_train__average)
                elif on == 'vor':
                    if var_criteria:
                        improved_ix.append(i)
                        improved_value.append(var_on_train__average)
                else:
                    raise Exception("Feature Selection Iterative: Down: Cannot decide by multiple target")

        improved_ix = numpy.array(improved_ix)
        improved_value = numpy.array(improved_value)

        if len(improved_ix) == 0:
            done = True

        if on == 'yor' or on == 'vor':
            max_ix = improved_value.argmax()
        else:
            raise Exception("Feature Selection Iterative: Down: Cannot decide by multiple target")

        if numpy.array(mask).sum() == 1:
            done = True
        else:
            mask[max_ix] = False

    return mask
