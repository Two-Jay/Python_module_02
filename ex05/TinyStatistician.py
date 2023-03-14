import math

class TinyStatistician():
    def __init__(self) -> None:
        pass

    def mean(self, x : list) -> float:
        if isinstance(x, list) == False:
            return None
        m = len(x) if isinstance(x, list) == True else 0
        if m == 0:
            return None
        ret = float(0)
        for i in x:
            ret += i
        return ret / m

    def median(self, x : list) -> float:
        if isinstance(x, list) == False:
            return None
        sorted_x = sorted(x)
        m = len(x) if isinstance(x, list) == True else 0
        if m == 0:
            return None
        elif m % 2 == 1:
            return sorted_x[(m + 1) // 2]
        else:
            median_index = m // 2
            return (sorted_x[median_index] + sorted_x[median_index + 1]) / 2

    # get the 1st and 3rd quartile
    def quartile(self, x : list) -> list:
        if isinstance(x, list) == False:
            return None
        m = len(x) if isinstance(x, list) == True else 0
        if m == 0:
            return None
        sorted_x = sorted(x)
        median_index = m // 2
        return [sorted_x[median_index // 2], sorted_x[median_index + median_index // 2]]
        
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

