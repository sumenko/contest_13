tests_ready = (
    ('Test #1: 0 m and n values',
    """0
0
""",''),
    ('Test #2: wrong n value',
    """5001
500
""", ''), 
    ('Test #3: wrong m value',
    """10
1001
""", ''),
    ('Test #4: push and pop back',
    """4
10
push_back 100
push_back 200
pop_back
pop_back
""", """200
100
"""),
    ('Test #5: push_back overflow',
    """4
3
push_back 1
push_back 2
push_back 3
push_back 4
""", """error
""")
)
tests_not_ready = (
    ('Test 1',
    """4
4
push_front 861
push_front -819
pop_back
pop_back
""", """861
-819
"""), 
    ('Test 2',
    """7
10
push_front -855
push_front 720
pop_back
pop_back
push_back 844
pop_back
push_back 823
""",
    """-855
720
844
"""
    )
)