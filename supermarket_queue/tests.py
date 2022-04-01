#!/usr/bin/env python3

# Tests:
def test_1(): assert queue_time([], 1) == 0

def test_2(): assert queue_time([5], 1) == 5

def test_3(): assert queue_time([2], 5) == 2

def test_4(): assert queue_time([1,2,3,4,5], 1) == 15

def test_5(): assert queue_time([1,2,3,4,5], 100) == 5

def test_6(): assert queue_time([2,2,3,3,4,4], 2) == 9

def test_7(): assert queue_time([2,2,3,3,4,4,5], 2) == 14
def test_8(): assert queue_time([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4], 4) == 10
def test_9(): assert queue_time([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4], 4) == 10
def test_10(): assert queue_time([1,1,1,1,2,2,2,2,3,3,3,3,4,4], 4) == 10
def test_11(): assert queue_time([1,1,1,1,2,2,2,2,3,3,3,3,4], 4) == 10

