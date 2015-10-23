from math import radians, degrees, sin, cos, atan2

if __name__ == "__main__":
	ans = 0
	for alpha in range(2, 91):
		print alpha
		for beta in range(alpha, 181 - alpha):
			for dag_alpha in range(1, min(alpha, 180 - beta)):
				for dag_beta in range(dag_alpha if alpha == beta else 1, min(beta, 180 - alpha)):
					a = sin(radians(dag_beta)) / sin(radians(alpha + dag_beta))
					b = sin(radians(beta)) / sin(radians(beta + dag_alpha))
					x = degrees(atan2(b * sin(radians(dag_alpha)) - a * sin(radians(alpha)), b * cos(radians(dag_alpha)) - a * cos(radians(alpha))))
					int_x = int(round(x, 0))
					if abs(x - int_x) >= 1e-9:
						continue
					delta = 180 - alpha + int_x
					gamma = 180 - beta - int_x
					if gamma < alpha:
						continue
					if delta < beta:
						continue
					if beta == delta and dag_alpha > alpha / 2:
						continue
					if gamma == alpha and dag_beta > beta / 2:
						continue
					ans += 1
	print ans
					
					