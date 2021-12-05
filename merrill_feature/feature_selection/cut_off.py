import numpy
import pandas


def cut_btw__multi_model(x_train, model, model_kwg, thresh=None, top=None):
    ...

    return None  # mask


def cut_btw__pair(x_train, method, thresh=None, top=None):
    if thresh is not None:

        mask = [True] * x_train.shape[1]
        codes = numpy.array(numpy.arange(x_train.shape[1]))
        done = False

        while not done:

            distance_matrix = numpy.abs(pandas.DataFrame(x_train[:, codes[mask]]).corr(method=method).values) - \
                              numpy.diag(numpy.ones(len(codes[mask])))
            distance_matrix_mask = distance_matrix >= thresh

            if distance_matrix_mask.sum() > 0:

                distance_matrix_mask_count = distance_matrix_mask.sum(axis=1)
                distance_matrix_mask_count_max = distance_matrix_mask_count.max()
                if (distance_matrix_mask_count == distance_matrix_mask_count_max).sum() == 1:
                    mask[codes[mask][distance_matrix_mask_count.argmax()]] = False
                else:
                    if distance_matrix.argmax() >= thresh:
                        distance_matrix_max_ix = numpy.unravel_index(distance_matrix.argmax(),
                                                                     shape=distance_matrix.shape)
                        if distance_matrix[distance_matrix_max_ix[0], :].max() >= \
                                distance_matrix[distance_matrix_max_ix[1], :].max():
                            mask[codes[mask][distance_matrix_max_ix[0]]] = False
                        else:
                            mask[codes[mask][distance_matrix_max_ix[1]]] = False

            else:
                done = True

            if numpy.array(mask).sum() == 1:
                done = True

    elif top is not None:

        mask = [True] * x_train.shape[1]
        codes = numpy.array(numpy.arange(x_train.shape[1]))

        distance_matrix = numpy.abs(pandas.DataFrame(x_train[:, codes[mask]]).corr(method=method).values) - \
                          numpy.diag(numpy.ones(codes[mask]))

        j = 0
        while j < top:
            distance_matrix_max_ix = numpy.unravel_index(distance_matrix.argmax(), shape=distance_matrix.shape)
            if distance_matrix[distance_matrix_max_ix[0], :].max() >= \
                    distance_matrix[distance_matrix_max_ix[1], :].max():
                mask[codes[mask][distance_matrix_max_ix[0]]] = False
            else:
                mask[codes[mask][distance_matrix_max_ix[1]]] = False
            j = j + 1
    else:
        raise Exception("Feature Selection Function: Cut Between Pair: Either 'thresh' or 'top' kwg should be passed")

    return mask


def cut_fwd__pair(x_train, y_train, method, thresh=None, top=None):
    if thresh is not None:

        mask = [True] * x_train.shape[1]
        codes = numpy.array(numpy.arange(x_train.shape[1]))
        done = False

        while not done:

            corr_to_target0 = numpy.abs(numpy.array([method(x_train[:, codes[mask]][:, j], y_train[:, 0])
                                                     for j in range(x_train[:, codes[mask]].shape[1])]))
            corr_to_target1 = numpy.abs(numpy.array([method(x_train[:, codes[mask]][:, j], y_train[:, 1])
                                                     for j in range(x_train[:, codes[mask]].shape[1])]))
            corr_to_targets_mask = (corr_to_target0 <= thresh) * (corr_to_target1 <= thresh)

            if corr_to_targets_mask.sum() > 0:
                mask[codes[mask][corr_to_targets_mask.argmax()]] = False
            else:
                done = True

            if numpy.array(mask).sum() == 1:
                done = True

    elif top is not None:

        mask = [True] * x_train.shape[1]
        codes = numpy.array(numpy.arange(x_train.shape[1]))

        corr_to_targets = numpy.abs(numpy.array([method(x_train[:, j], y_train) for j in range(x_train.shape[1])]))

        j = 0
        while j < top:
            mask[codes[mask][corr_to_targets.argmax()]] = False
            j = j + 1
    else:
        raise Exception("Feature Selection Function: Cut Forward Pair: Either 'thresh' or 'top' kwg should be passed")

    return mask
