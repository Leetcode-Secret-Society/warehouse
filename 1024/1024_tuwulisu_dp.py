class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key=lambda x: x[0])
        clip_count = len(clips)
        dp = [0]+[clip_count+1]*(time)
        for clip in clips:
            i = clip[0] + 1
            j = clip[1] + 1
            for k in range(i, min(j, time+1)):
                dp[k] = min(dp[i-1]+1, dp[k])
            #print(dp)
        return dp[-1] if dp[-1]!=clip_count+1 else -1
