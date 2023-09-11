class LazySegmentTree:
    """
    反转区间中的 0 / 1 的 线段数模板, 记录的是[l, r] 中 1 的个数
    """
    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums
        self.ones = [0] * (4 * self.n)
        self.lazy = [False] * (4 * self.n)
        self._build(0, 0, self.n-1)

    def _build(self, idx: int, l: int, r: int) -> None:
        if l == r:
            self.ones[idx] = self.nums[l]
            return

        mid = (l + r) >> 1
        self._build(2 * idx + 1, l, mid)
        self._build(2 * idx + 2, mid + 1, r)
        self.ones[idx] = self.ones[2 * idx + 1] + self.ones[2 * idx + 2]

    def _do(self, idx: int, l: int, r: int) -> None:
        self.ones[idx] = r - l + 1 - self.ones[idx]
        self.lazy[idx] = not self.lazy[idx]

    def _pushdown(self, idx: int, l: int, r: int) -> None:
         if self.lazy[idx]:
             mid = (l + r) >> 1
             self._do(2 * idx + 1, l, mid)
             self._do(2 * idx + 2, mid + 1, r)
             self.lazy[idx] = False

    def _update(self, idx: int, l: int, r: int, ql: int, qr: int) -> None:
        if ql <= l and r <= qr:
            self._do(idx, l, r)
            return

        self._pushdown(idx, l, r)
        mid = (l + r) >> 1
        if ql <= mid:
            self._update(2 * idx + 1, l, mid, ql, qr)
        if qr > mid:
            self._update(2 * idx + 2, mid + 1, r, ql, qr)
        self.ones[idx] = self.ones[2 * idx + 1] + self.ones[2 * idx + 2]

    def _query(self, idx: int , l: int, r:int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:
            return self.ones[idx]

        mid = (l + r) >> 1
        self._pushdown(idx, l, r)
        ans = 0
        if ql <= mid:
            ans += self._query(2 * idx + 1, l, mid, ql, qr)
        if qr > mid:
            ans += self._query(2 * idx + 2, mid + 1, r, ql, qr)
        return ans

    def update(self, ql: int, qr: int) -> None:
        self._update(0, 0, self.n - 1, ql, qr)

    def query(self, ql: int, qr: int) -> int:
        return self._query(0, 0, self.n - 1, ql, qr)

if __name__ == '__main__':
    st = LazySegmentTree([1, 0, 1, 1, 1])
    print(st.ones)