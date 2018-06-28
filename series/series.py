def slices(series, length):
    series_len = len(series)

    if not series:
        raise ValueError("`series` must be non-empty string.")
    if not 0 < length <= series_len:
        raise ValueError("`length` must positive and less-equal `len(series)={}`.".format(series_len))

    return [
        series[i:i + length]
        for i
        in range(0, series_len - length + 1)
    ]
