from utilidades.lane import xm_per_pix as x


def offCenter(meanPts, inpFrame):
    mpts = meanPts[-1][-1][-2].astype(int)
    pixelDeviation = inpFrame.shape[1] / 2 - abs(mpts)
    deviation = pixelDeviation * x
    direction = "esquerda" if deviation < 0 else "direita"

    return deviation, direction
