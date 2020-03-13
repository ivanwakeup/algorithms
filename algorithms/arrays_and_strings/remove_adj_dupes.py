class Solution:
    def removeDuplicates(self, S: str) -> str:
        arr = list(S)
        cont = True
        while cont:
            for i, char in enumerate(arr):
                if i > 0 and arr[i] == arr[i - 1]:
                    arr = arr[:i - 1] + arr[i + 1:]
                    break
                if i == len(arr) - 1:
                    cont = False
                    break

        return "".join(arr)

sol = Solution()

print(
sol.removeDuplicates("abbaca")
)