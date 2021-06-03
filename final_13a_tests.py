tests = (
    ('Smoke test 1',
    """0
0
""",''),
    ('Smoke test 2',
    """5001
500
""", ''), 
    ('Smoke test 3',
    """10
1001
""", ''),
    ('Smoke test 4',
    """4
10
push_back 100
push_back 200
pop_back
pop_back
""", """200
100
"""),
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