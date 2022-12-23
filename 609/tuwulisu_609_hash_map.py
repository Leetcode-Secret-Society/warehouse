class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_filepath_dict = defaultdict(list)
        for path in paths:
            parts = path.split(' ')
            dir_ = parts[0]
            files = parts[1:]
            for file in files:
                file_parts = file.split('(')
                filename = file_parts[0]
                content = file_parts[1][:-1]
                filepath = f"{dir_}/{filename}"
                content_filepath_dict[content].append(filepath)
        return [filepath_list for filepath_list in content_filepath_dict.values() if len(filepath_list)>1]
