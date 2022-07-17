class Solution:
    def floodFill(self, image, sr, sc, color):
        starting_color = image[sr][sc]
        if starting_color == color:
            return image
        n = len(image)
        m = len(image[0])
        r, c = sr, sc
        
        visited = {(sr, sc)}
        def flood_dfs(r, c):
            visited.add((r, c))
            if r < 0 or c < 0 or r >= n or c >= m or image[r][c] != starting_color:
                return
            image[r][c] = color
            flood_dfs(r+1, c)
            flood_dfs(r-1, c)
            flood_dfs(r, c+1)
            flood_dfs(r, c-1)
             
                
                    
        flood_dfs(r, c)
        print(visited)
        return image


S = Solution()
retval = S.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
print(retval)

# ret2 = S.floodFill([[0,0,0],[0,0,0]], 0, 0, 0)
# print(ret2)