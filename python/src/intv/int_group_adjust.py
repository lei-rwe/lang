import pytest
from datetime import datetime
import numpy as np

# Your task is to write the group adjustment method below. There are some
# unimplemented unit_tests at the bottom which also need implementation.
# Your solution can be pure python, pure NumPy, pure Pandas
# or any combination of the three.  There are multiple ways of solving this
# problem, be creative, use comments to explain your code.

# Group Adjust Method
# The algorithm needs to do the following:
# 1.) For each group-list provided, calculate the means of the values for each
# unique group.
#
#   For example:
#   vals       = [  1  ,   2  ,   3  ]
#   ctry_grp   = ['USA', 'USA', 'USA']
#   state_grp  = ['MA' , 'MA' ,  'CT' ]
#
#   There is only 1 country in the ctry_grp list.  So to get the means:
#     USA_mean == mean(vals) == 2
#     ctry_means = [2, 2, 2]
#   There are 2 states, so to get the means for each state:
#     MA_mean == mean(vals[0], vals[1]) == 1.5
#     CT_mean == mean(vals[2]) == 3
#     state_means = [1.5, 1.5, 3]
#
# 2.) Using the weights, calculate a weighted average of those group means
#   Continuing from our example:
#   weights = [.35, .65]
#   35% weighted on country, 65% weighted on state
#   ctry_means  = [2  , 2  , 2]
#   state_means = [1.5, 1.5, 3]
#   weighted_means = [2*.35 + .65*1.5, 2*.35 + .65*1.5, 2*.35 + .65*3]
#
# 3.) Subtract the weighted average group means from each original value
#   Continuing from our example:
#   val[0] = 1
#   ctry[0] = 'USA' --> 'USA' mean == 2, ctry weight = .35
#   state[0] = 'MA' --> 'MA'  mean == 1.5, state weight = .65
#   weighted_mean = 2*.35 + .65*1.5 = 1.675
#   demeaned = 1 - 1.675 = -0.675
#   Do this for all values in the original list.
#
# 4.) Return the demeaned values

# Hint: See the test cases below for how the calculation should work.

def adjust_on_group(vals, group, weight):
    '''
    Calculate the mean for a given group
    :return: an iterator which holds the value to adjust for the given group and weight
    '''
    import itertools
    if len(vals) != len(group):
        raise ValueError("values and groups have different sizes")
    dict = {}
    for v, g in  itertools.izip(vals, group):
        if not v: continue
        if g in dict and dict[g]['sum']:
            dict[g]['sum'] += v
            dict[g]['count'] += 1
        else:
            dict[g] = {'sum': v, 'count': 1}

    for (k, v) in dict.items():
        dict[k]['adjust'] = float(weight) * v['sum'] / v['count']
    # print dict

    for v, g in  itertools.izip(vals, group):
        yield dict[g]['adjust']

def group_to_int(group):
    '''
    Given a list of group values, change it to int so that
    the values can be used as index
    Note: the values of group will be changed to int
    :return: the max of the values in the group
    '''
    dict = {}   # its values like {'NJ':0, 'NY':1}
    value = 0
    for i in range(0, len(group)):
        g = group[i]
        if not g: continue      # Keep None
        if g in dict:
            group[i] = dict[g]
        else:
            dict[g] = value
            group[i] = value
            value += 1
    return value

def test_group_to_int():
    vals = [1, None, 3, 5, 8, 7]
    grps_1 = ['USA']
    grps_2 = ['MA', 'RI', 'RI', 'CT', 'CT', 'CT', 'RI', 'CT', 'RI', 'NJ', 'NJ', 'CT', 'NJ']
    i = group_to_int(vals)
    print vals
    print i

    i = group_to_int(grps_1)
    print grps_1
    print i

    i = group_to_int(grps_2)
    print grps_2
    print i

def adjust_on_int_group(vals, group, group_max, weight):
    '''
    If we know that values in group are in a given range [0, group_max),
    we do not need to use hash dictionarly. We can use array instead
    Calculate the mean for a given group
    :return: an iterator which holds the value to adjust for the given group and weight
    '''
    import itertools
    if len(vals) != len(group):
        raise ValueError("values and groups have different sizes")

    sums = [0] * group_max
    cnts = [0] * group_max
    for v, g in  itertools.izip(vals, group):
        if not v: continue
        sums[g] += v
        cnts[g] += 1
    # print sums
    # print cnts

    for v, g in  itertools.izip(vals, group):
        yield float(weight) * sums[g] / cnts[g]

def int_group_adjust(vals, groups, weights):
    if len(groups) != len(weights):
        raise ValueError("groups and weights have different sizes")

    weight_index = 0
    adj_vals = list(vals)
    for group in groups:
        group_max = group_to_int(group)
        vi = 0
        for v in adjust_on_int_group(vals, group, group_max, weights[weight_index]):
            if v and adj_vals[vi]:
                adj_vals[vi] -= v
            vi += 1
        weight_index += 1

    # print map(lambda x : '{0:0.3f}'.format(x) if x else None, adj_vals)
    return adj_vals

def group_adjust(vals, groups, weights):
    """
    Calculate a group adjustment (demean).

    Parameters
    ----------

    vals    : List of floats/ints

        The original values to adjust

    groups  : List of Lists

        A list of groups. Each group will be a list of ints

    weights : List of floats

        A list of weights for the groupings.

    Returns
    -------

    A list-like demeaned version of the input values
    """
    if len(groups) != len(weights):
        raise ValueError("groups and weights have different sizes")

    weight_index = 0
    adj_vals = list(vals)
    for group in groups:
        vi = 0
        for v in adjust_on_group(vals, group, weights[weight_index]):
            if v and adj_vals[vi]:
                adj_vals[vi] -= v
            vi += 1
        weight_index += 1

    # print map(lambda x : '{0:0.3f}'.format(x) if x else None, adj_vals)
    return adj_vals

def test_three_groups():
    vals = [1, 2, 3, 8, 5]
    grps_1 = ['USA', 'USA', 'USA', 'USA', 'USA']
    grps_2 = ['MA', 'MA', 'MA', 'RI', 'RI']
    grps_3 = ['WEYMOUTH', 'BOSTON', 'BOSTON', 'PROVIDENCE', 'PROVIDENCE']
    weights = [.15, .35, .5]

    adj_vals = group_adjust(vals, [grps_1, grps_2, grps_3], weights)
    int_group_adjust(vals, [grps_1, grps_2, grps_3], weights)
    # 1 - (USA_mean*.15 + MA_mean * .35 + WEYMOUTH_mean * .5)
    # 2 - (USA_mean*.15 + MA_mean * .35 + BOSTON_mean * .5)
    # 3 - (USA_mean*.15 + MA_mean * .35 + BOSTON_mean * .5)
    # etc ...
    # Plug in the numbers ...
    # 1 - (.15*2 + .35*2 + .5*1)   # -0.5
    # 2 - (.15*2 + .35*2 + .5*2.5) # -.25
    # 3 - (.15*2 + .35*2 + .5*2.5) # 0.75
    # etc...

    answer = [-0.770, -0.520, 0.480, 1.905, -1.095]
    for ans, res in zip(answer, adj_vals):
        assert abs(ans - res) < 1e-5


def test_two_groups():
    vals = [1, 2, 3, 8, 5]
    grps_1 = ['USA', 'USA', 'USA', 'USA', 'USA']
    grps_2 = ['MA', 'RI', 'CT', 'CT', 'CT']
    weights = [.65, .35]

    adj_vals = group_adjust(vals, [grps_1, grps_2], weights)
    int_group_adjust(vals, [grps_1, grps_2], weights)
    # 1 - (.65*2 + .35*1)   # -0.65
    # 2 - (.65*2 + .35*2.5) # -.175
    # 3 - (.65*2 + .35*2.5) # -.825
    answer = [-1.81999, -1.16999, -1.33666, 3.66333, 0.66333]
    for ans, res in zip(answer, adj_vals):
        assert abs(ans - res) < 1e-5


def test_missing_vals():
    # If you're using NumPy or Pandas, use np.NaN
    # If you're writing pyton, use None
    # vals = [1, np.NaN, 3, 5, 8, 7]
    vals = [1, None, 3, 5, 8, 7]
    grps_1 = ['USA', 'USA', 'USA', 'USA', 'USA', 'USA']
    grps_2 = ['MA', 'RI', 'RI', 'CT', 'CT', 'CT']
    weights = [.65, .35]

    adj_vals = group_adjust(vals, [grps_1, grps_2], weights)
    int_group_adjust(vals, [grps_1, grps_2], weights)

    # This should be None or np.NaN depending on your implementation
    # please feel free to change this line to match yours
    # answer = [-2.47, np.NaN, -1.170, -0.4533333, 2.54666666, 1.54666666]
    answer = [-2.47, None, -1.170, -0.4533333, 2.54666666, 1.54666666]

    for ans, res in zip(answer, adj_vals):
        if ans and res:
            assert abs(ans - res) < 1e-5
        elif ans is None:
            assert res is None
        elif np.isnan(ans):
            assert np.isnan(res)

def test_weights_len_equals_group_len():
    # Need to have 1 weight for each group

    # vals = [1, np.NaN, 3, 5, 8, 7]
    vals = [1, None, 3, 5, 8, 7]
    grps_1 = ['USA', 'USA', 'USA', 'USA', 'USA', 'USA']
    grps_2 = ['MA', 'RI', 'RI', 'CT', 'CT', 'CT']
    weights = [.65]

    with pytest.raises(ValueError) as ve:
        group_adjust(vals, [grps_1, grps_2], weights)

    # print ve


def test_group_len_equals_vals_len():
    # The groups need to be same shape as vals
    vals = [1, None, 3, 5, 8, 7]
    grps_1 = ['USA']
    grps_2 = ['MA', 'RI', 'RI', 'CT', 'CT', 'CT']
    weights = [.65]

    with pytest.raises(ValueError):
        group_adjust(vals, [grps_1, grps_2], weights)


def test_performance():
    C = 1000000
    vals = C *[1, None, 3, 5, 8, 7]
    # If you're doing numpy, use the np.NaN instead
    # vals = C * [1, np.NaN, 3, 5, 8, 7]
    grps_1 = C * [1, 1, 1, 1, 1, 1]
    grps_2 = C * [1, 1, 1, 1, 2, 2]
    grps_3 = C * [1, 2, 2, 3, 4, 5]
    weights = [.20, .30, .50]

    start = datetime.now()
    int_group_adjust(vals, [grps_1, grps_2, grps_3], weights)
    end = datetime.now()
    diff = end - start
    print 'Total performance test time: {}'.format(diff.total_seconds())

if __name__ == "__main__":
    print "------------ test group to int"
    test_group_to_int()
    print "------------ test three groups"
    test_three_groups()
    print "------------ test two groups"
    test_two_groups()
    print "------------ test missing values"
    test_missing_vals()
    print "------------ test weights len equals group len"
    test_weights_len_equals_group_len()
    print "------------ test group len equals values len"
    test_group_len_equals_vals_len()
    print "------------ test performance"
    test_performance()
