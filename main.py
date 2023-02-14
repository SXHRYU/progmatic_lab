from typing import List


def main(num: str = "9876543210", target: int = 200) -> List[str]:
    res: List[str] = []

    def dfs(cur_idx: int, cur_res: List[str], cur_sum: int) -> None:
        if cur_idx >= len(num):
            if cur_sum == target:
                res.append("".join(cur_res))
            return

        else:
            for i in range(cur_idx, len(num)):
                cur_str: str = num[cur_idx : i + 1]
                cur_num: int = int(cur_str)

                if not cur_res:
                    # root and far-right branch entry
                    dfs(i + 1, [cur_str], cur_num)
                else:
                    dfs(i + 1, cur_res + ["+"] + [cur_str], cur_sum + cur_num)
                    dfs(i + 1, cur_res + ["-"] + [cur_str], cur_sum - cur_num)

    dfs(0, [], 0)
    return res


print(main("9876543210", 200))
