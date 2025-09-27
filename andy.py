def greeting(name, surname=None):
	"""Print a greeting.

	Args:
		name (str): First name to greet.
		surname (str|None): Optional surname. If provided, included in the greeting.
	"""
	if surname:
		print(f"hello {name} {surname}")
	else:
		print(f"hello {name}")


if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(description="Greet people by full name.")
	parser.add_argument(
		"names",
		nargs="*",
		help="Full names to greet (e.g. 'Ramon Geronimo'). If omitted, defaults are used.",
	)
	args = parser.parse_args()

	defaults = ["andy", "Alice Smith", "Ramon Geronimo", "Jessie Pichardo"]
	to_greet = args.names if args.names else defaults

	def greeting_from_full(full_name):
		parts = full_name.split()
		if len(parts) == 0:
			return
		if len(parts) == 1:
			greeting(parts[0])
		else:
			greeting(parts[0], " ".join(parts[1:]))

	for full in to_greet:
		greeting_from_full(full)
		# end of script


	def make_pbj(bread_type="white", peanut_butter="creamy", jelly="grape"):
		"""Print steps to make a peanut butter and jelly sandwich.

		Args:
			bread_type (str): Type of bread to use.
			peanut_butter (str): Type of peanut butter.
			jelly (str): Type of jelly or jam.
		"""
		steps = [
			f"Take two slices of {bread_type} bread.",
			f"Spread {peanut_butter} peanut butter on one slice.",
			f"Spread {jelly} jelly on the other slice.",
			"Put the two slices together with the spreads facing each other.",
			"Cut the sandwich in half (optional).",
			"Serve and enjoy!",
		]
		for i, s in enumerate(steps, start=1):
			print(f"{i}. {s}")