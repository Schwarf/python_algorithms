from dynamic_programming.count_unique_binary_search_trees import count_unique_bst_recursive, \
    count_count_unique_bst_bottom_up


def test_count_bst_n_is_1():
    n = 1
    expected_result = 1
    assert expected_result == count_unique_bst_recursive(n)


def test_count_bst_n_is_3():
    n = 3
    expected_result = 5
    assert expected_result == count_unique_bst_recursive(n)


def test_count_bst_n_is_10():
    n = 10
    expected_result = 16796
    assert expected_result == count_unique_bst_recursive(n)



#############################################################
#############################################################
#############################################################


def test_count_bst_top_down_n_is_1():
    n = 1
    expected_result = 1
    assert expected_result == count_count_unique_bst_bottom_up(n)


def test_count_bst_top_down_n_is_3():
    n = 3
    expected_result = 5
    assert expected_result == count_count_unique_bst_bottom_up(n)


def test_count_bst_top_down_n_is_10():
    n = 10
    expected_result = 16796
    assert expected_result == count_count_unique_bst_bottom_up(n)


def test_count_bst_top_down_n_is_19():
    n = 19
    expected_result = 1767263190
    assert expected_result == count_count_unique_bst_bottom_up(n)
