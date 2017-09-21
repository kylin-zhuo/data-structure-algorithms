class Solution(object):

	def solution(self, time):

		h, m = time.split(":")
		digits = set(h).union(set(m))

		cand_all = [int(a+b) for a in digits for b in digits]
		cand_h = sorted(filter(lambda x:x<24, cand_all))
		cand_m = sorted([c for c in cand_all if c < 60])

		i, j = cand_h.index(int(h)), cand_m.index(int(m))

		if j < len(cand_m) - 1:
			ret_h, ret_m = h, cand_m[j+1]
		else:
			ret_h, ret_m = cand_h[i+1] if i < len(cand_h)-1 else cand_h[0], cand_m[0]

		return ('0'+str(ret_h))[-2:] + ":" + ('0'+str(ret_m))[-2:]


for h in range(24):
	for m in range(60):
		time = ('0'+str(h))[-2:] + ":" + ('0'+str(m))[-2:]
		print time + "->" + Solution().solution(time)