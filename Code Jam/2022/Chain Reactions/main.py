import sys

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return list(map(int, input().split()))

def get_fun_value(nodes, key):

    fun_list = []

    while key != 0:
        fun_list.append(nodes.get(key))
        key = nodes.get(key)[1]

    return sorted(fun_list, key=lambda x: x[0])

def get_all_fun(nodes, inicializators):

    fun_init = {
        init_: get_fun_value(nodes, init_) for init_ in inicializators
    }

    return fun_init

def get_first_node(fun_init):

    i = 1
    max_values = set(
        ["_".join([str(j) for j in value[-i]]) for value in fun_init.values()]
    )

    max_len = max([len(value) for value in fun_init.values()])

    while (len(max_values) != len(fun_init)) and (i <= max_len):
        i += 1
        max_values = set(
            ["_".join([str(j) for j in value[-i]]) 
            if i <= len(value) else "_".join([str(j) for j in value[0]]) 
            for value in fun_init.values()]
        )
        # print(max_values)
        # print(i)

    sum_max_values = [
        [key, sum([k[0] for k in values][-i:])] for key, values in fun_init.items()
    ]

    min_sum_key = sorted(sum_max_values, key=lambda x: x[1])[0][0]

    return min_sum_key


def delete_node_and_edges(nodes, key):

    while key != 0:
        key_ = nodes.get(key)[1]
        del nodes[key]
        key = key_


def clean_dict(nodes):

    keys_ = list(nodes.keys())

    # print("clean_dict")
    # print(nodes)
    for key in keys_:
        if nodes[key][1] not in keys_:
            nodes[key][1] = 0
    # print(nodes)


t = read()

for t_ in range(t):
    
    N = read()
    nodes = {
        j: [fun, con] for j, fun, con in zip(
            [i for i in range(1, N+1)], read_line(), read_line()
        )
    }
    ans = []

    inicializators = list(
        set(nodes.keys()) - set([i[1] for i in nodes.values()])
    )
    
    
    while len(nodes) != 0:
        # print('\n\nnodes:', nodes)
        # print("inicializators",  inicializators)

        fun_init = get_all_fun(nodes, inicializators)
        
        # print("fun_init", fun_init)

        first_node = get_first_node(fun_init)

        # print(first_node)
        # print(fun_init.get(first_node))
        ans.append(
            max([p[0] for p in fun_init.get(first_node)])
        )

        inicializators.remove(first_node)
        delete_node_and_edges(nodes, first_node)
        clean_dict(nodes)

    # print(ans)
    print(f"Case #{t_+1}: {sum(ans)}")