class LazySegmentTree:
    """
   	update使用的是覆盖式, 记录的是[l, r] 中的最大值
    """
    def __init__(self, n: int):
        self.n = n
        self.mx = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def _pushdown(self, o:int) -> None:
        if self.lazy[o] == 0:
            return

        self.mx[2 * o + 1] = self.lazy[o]
        self.mx[2 * o + 2] = self.lazy[o]
        self.lazy[2 * o + 1] = self.lazy[o]
        self.lazy[2 * o + 2] = self.lazy[o]
        self.lazy[o] = 0

    def _update(self, o: int, l: int, r: int, ql: int, qr: int, h: int) -> None:
        if ql <= l and r <= qr:
            self.mx[o] = h
            self.lazy[o] = h
            return

        self._pushdown(o)
        mid = (l+ r) >> 1
        if ql <= mid:
            self._update(2* o + 1, l, mid, ql, qr, h)
        if qr > mid:
            self._update(2 * o + 2, mid + 1, r, ql, qr, h)
        self.mx[o] = max(self.mx[2* o + 1], self.mx[2*o + 2])

    def _query(self, o: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:
            return self.mx[o]

        self._pushdown(o)
        ans = 0
        mid = (l + r) >> 1
        if ql <= mid:
            ans = max(ans,self._query(2 * o + 1, l, mid, ql, qr))
        if qr > mid:
            ans = max(ans, self._query(2 * o + 2, mid + 1, r, ql, qr))
        return ans

    def query(self, ql: int, qr: int) -> int:
        return self._query(0, 0, self.n-1, ql, qr)

    def update(self, ql: int, qr:int, h: int) -> None:
        self._update(0, 0, self.n-1, ql, qr, h)


if __name__ == '__main__':
    nums = [1, 3, 5]
    n = len(nums)
    st = LazySegmentTree(n)
    for i, num in enumerate(nums):
        st.update(i, i, num)
        print(st.mx)