import gulp_test as gtest

@gtest.test('iter_chain')
@gtest.no_errors
def test_iter_chain():
    from extendly import extensions
    from extendly.iter_chain import iter_chain

    with extensions(iter_chain):
        [1, 2, 3].map(lambda x: x ** x).filter(lambda x: x == 4).apply(list).apply(print)

@gtest.test('num_times')
@gtest.no_errors
def test_num_times():
    from extendly import extensions
    from extendly.num_times import num_times

    with extensions(num_times):
        (5).times(lambda: print('hi'))

@gtest.test('num_times & iter_chain')
@gtest.no_errors
def test_num_and_iter():
    from extendly import extensions
    from extendly.num_times import num_times
    from extendly.iter_chain import iter_chain

    with extensions(iter_chain, num_times):
        [1, 2, 3].map(lambda x: x.times(lambda: print(x))).apply(list)

@gtest.test('func_partial')
@gtest.no_errors
def test_func_partial():
    from extendly import extensions
    from extendly.func_partial import func_partial

    with extensions(func_partial):
        print.partial('hello')()

@gtest.test('func_partial & num_times')
@gtest.no_errors
def test_partial_and_num():
    from extendly import extensions
    from extendly.num_times import num_times
    from extendly.func_partial import func_partial

    with extensions(num_times, func_partial):
        (5).times(print.partial('hi'))

@gtest.test('func_partial & num_times & iter_chain')
@gtest.no_errors
def test_partial_and_num_and_iter():
    from extendly import extensions
    from extendly.num_times import num_times
    from extendly.func_partial import func_partial
    from extendly.iter_chain import iter_chain

    with extensions(num_times, iter_chain, func_partial):  
        [1, 2, 3].map(int.times.partial(func=print.partial('hey'))).apply(list)


gtest.do_tests()
