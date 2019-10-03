import random

edges = []
with open("input.txt", "r") as file:
	for line in file:
		edges.append(line.strip().split(" -> "))

def get_adjacent_edges(pos, edges):
	choices = []
	for edge in edges:
		if pos == edge[0]:
			choices.append(edge[1])
	return choices

split_edges = []
for edge in edges:
	if len(edge[1]) > 1:
		split = edge[1].split(',')
		for item in split:
			split_edges.append([edge[0], item])
	else:
		split_edges.append([edge[0], edge[1]])

def check_edges(edges):
	start = [x[0] for x in edges]
	end = [x[1] for x in edges]
	vertices = set(start).union(set(end))
	in_dict = {x : 0 for x in vertices}
	out_dict = {x : 0 for x in vertices}
	for edge in edges:
		out_dict[edge[0]] += 1
		in_dict[edge[1]] += 1
	for vertex in vertices:
		if out_dict[vertex] > in_dict[vertex]:
			x = vertex
	if x:
		return x
	else:
		return random.sample(vertices, 1)

split_edges = [list(map(int, x)) for x in split_edges]

stack = []
circuit = []

pos = check_edges(split_edges)
print(pos)

while len(split_edges) > 0:
	choices = get_adjacent_edges(pos, split_edges)
	while choices == []:
		circuit.append(pos)
		pos = stack.pop()
		choices = get_adjacent_edges(pos, split_edges)
	stack.append(pos)
	pos = random.choice(choices)
	split_edges.remove([stack[-1], pos])
stack.append(pos)

while len(stack) > 0:
	circuit.append(stack.pop())

circuit = list(map(str, circuit))
output = open('output.txt', 'w')
output.write('->'.join(circuit[::-1]))