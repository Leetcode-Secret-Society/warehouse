class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        sub_versions_1 = version1.split(".")
        sub_versions_2 = version2.split(".")
        sub_versions_1_length = len(sub_versions_1)
        sub_versions_2_length = len(sub_versions_2)
        for i in range(max(sub_versions_1_length, sub_versions_2_length)):
            sub_version_1 = sub_version_2 = 0
            if i < sub_versions_1_length:
                sub_version_1 = int(sub_versions_1[i])
            if i < sub_versions_2_length:
                sub_version_2 = int(sub_versions_2[i])

            if sub_version_1 > sub_version_2:
                return 1
            elif sub_version_1 < sub_version_2:
                return -1

        return 0