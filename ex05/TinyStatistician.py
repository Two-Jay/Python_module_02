import math
import statistics as st

class TinyStatistician():
    def __init__(self) -> None:
        pass

    def mean(self, x : list) -> float:
        if isinstance(x, list) == False or len(x) == 0:
            return None
        return float(st.mean(x))

    def median(self, x : list) -> float:
        if isinstance(x, list) == False:
            return None
        m = len(x) if isinstance(x, list) == True else 0
        if m == 0:
            return None
        return st.median(x)

    # get the 1st and 3rd quartile
    def quartile(self, x : list) -> list:
        if isinstance(x, list) == False or len(x) == 0:
            return None
        quantiles = st.quantiles(sorted(x), n=4)
        return [quantiles[0], quantiles[2]]
        
    def var(self, x : list) -> float:
        if isinstance(x, list) == False:
            return None
        m = len(x) if isinstance(x, list) == True else 0
        if m == 0:
            return None
        mean_x = self.mean(x)
        ret = float(0)
        for i in x:
            ret += math.pow(i - mean_x, 2)
        return ret / m

    def std(self, x : list) -> float:
        return math.sqrt(self.var(x))
    

if __name__ == "__main__":
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]

    print(f"mean: {tstat.mean(a)}")
    print(f"median: {tstat.median(a)}")
    print(f"quartile: {tstat.quartile(a)}")
    print(f"variance: {tstat.var(a)}")
    print(f"standard deviation: {tstat.std(a)}")
