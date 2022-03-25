#some test cases for you...
test.expect(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), 'should return True');
test.expect(not is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), 'should return False');
test.expect(not is_valid_walk(['w']), 'should return False');
test.expect(not is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), 'should return False');


Time: 475ms Passed: 210Failed: 0
Test Results:
Walk Validator - basic tests
should return false if walk is too short
(2 of 2 Assertions)
should return false if walk is too long
(2 of 2 Assertions)
should return false if walk does not bring you back to start
(2 of 2 Assertions)
should return true for a valid walk
(4 of 4 Assertions)
Walk Validator - random tests
Testing a ['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's'] walk
Testing a ['s', 'n', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'] walk
Testing a ['s', 'w', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'] walk
Testing a ['n', 'w', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['n', 's', 'e', 's', 'n', 's', 'e', 'w', 'n', 's'] walk
Testing a ['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['n', 'w', 'w', 'w', 'n', 's', 'e', 'w', 'n', 's'] walk
Testing a ['n', 'w', 'e', 's', 'n', 's', 'e', 'w', 'n', 's'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['n', 'w', 'e', 's', 'n', 's', 'e', 'w', 'n', 's'] walk
Testing a ['n', 'w', 'w', 'w', 's', 's', 'e', 'w', 'n', 's'] walk
Testing a ['e', 'w', 'e', 'w', 'n', 'w', 'n', 's', 'e', 'w'] walk
Testing a ['n', 'w', 'w', 'w', 's', 's', 'n', 'w', 'n', 's'] walk
Testing a ['e', 'w', 'w', 'w', 'n', 'w', 'n', 's', 'e', 'w'] walk
Testing a ['n', 'w', 'e', 's', 'n', 's', 'e', 'w', 'n', 's'] walk
Testing a ['e', 'w', 'w', 'w', 'n', 'w', 'n', 's', 'e', 'w'] walk
Testing a ['e', 'w', 'w', 'w', 'n', 'w', 'n', 's', 'e', 'w'] walk
Testing a ['e', 'w', 'w', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['n', 'w', 'w', 'w', 's', 's', 'n', 'w', 'n', 's'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['e', 'w', 'w', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['n', 'w', 'w', 'w', 's', 's', 'n', 'w', 'n', 's'] walk
Testing a ['n', 'w', 'w', 'w', 's', 's', 'w', 'w', 'n', 's'] walk
Testing a ['n', 'w', 'w', 'w', 's', 's', 'w', 's', 'n', 's'] walk
Testing a ['e', 'w', 'w', 'w', 'n', 'e', 'n', 's', 'e', 'w'] walk
Testing a ['n', 'w', 'w', 'w', 's', 's', 'w', 's', 'n', 's'] walk
Testing a ['n', 'w', 'w', 'w', 's', 's', 'w', 's', 'n', 's'] walk
Testing a ['n', 'w', 'e', 's', 'n', 's', 'e', 'w', 'n', 's'] walk
Testing a ['n', 'w', 's', 'w', 's', 's', 'w', 's', 'n', 's'] walk
Testing a ['e', 'w', 'w', 'w', 'n', 'e', 'n', 's', 'e', 'w'] walk
Testing a ['e', 'w', 'w', 'w', 'n', 'e', 'n', 's', 'e', 'w'] walk
Testing a ['n', 'w', 's', 'w', 's', 's', 'w', 's', 'n', 's'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['n', 'w', 'e', 's', 'n', 's', 'e', 'w', 'n', 's'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['e', 'w', 'w', 'w', 'n', 'e', 'n', 's', 'e', 'w'] walk
Testing a ['n', 'w', 's', 's', 'n', 's', 'e', 'w', 'n', 's'] walk
Testing a ['n', 'w', 's', 's', 'n', 'n', 'e', 'w', 'n', 's'] walk
Testing a ['e', 'w', 'w', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['n', 'w', 's', 'w', 's', 's', 'w', 's', 'e', 's'] walk
Testing a ['e', 'n', 'w', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['n', 'w', 's', 's', 'n', 'n', 'e', 'w', 'n', 's'] walk
Testing a ['e', 'n', 'w', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['n', 'w', 's', 'w', 's', 's', 'w', 's', 'e', 's'] walk
Testing a ['e', 'n', 'w', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['e', 'n', 'w', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['e', 'n', 'n', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['n', 'w', 's', 'w', 's', 's', 'w', 's', 'e', 's'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['w', 'n', 'n', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['n', 'w', 's', 'w', 's', 's', 'w', 's', 'e', 's'] walk
Testing a ['n', 'w', 's', 'w', 's', 's', 'w', 's', 'e', 's'] walk
Testing a ['n', 'w', 's', 'n', 's', 's', 'w', 's', 'e', 's'] walk
Testing a ['w', 'n', 'n', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['w', 'n', 'n', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['n', 'w', 'w', 'n', 's', 's', 'w', 's', 'e', 's'] walk
Testing a ['n', 'w', 's', 's', 'n', 'n', 'e', 'w', 'n', 's'] walk
Testing a ['w', 'n', 'n', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['n', 'w', 'w', 'n', 's', 's', 'w', 's', 'e', 's'] walk
Testing a ['n', 'w', 's', 's', 'n', 'n', 'e', 'w', 'n', 's'] walk
Testing a ['w', 'n', 'n', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['n', 'w', 'w', 'n', 's', 's', 'w', 's', 'e', 's'] walk
Testing a ['n', 'w', 's', 's', 'n', 'n', 'e', 'w', 'n', 's'] walk
Testing a ['w', 'n', 'n', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['n', 'w', 's', 's', 'n', 'n', 'e', 'n', 'n', 's'] walk
Testing a ['s', 'w', 'w', 'n', 's', 's', 'w', 's', 'e', 's'] walk
Testing a ['w', 'n', 'n', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['w', 'n', 'n', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['n', 'w', 's', 's', 'n', 'n', 'e', 'n', 'n', 's'] walk
Testing a ['w', 'n', 'n', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['w', 'n', 'n', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['s', 'w', 'w', 'n', 's', 's', 'w', 's', 'e', 's'] walk
Testing a ['w', 'n', 'n', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['s', 'w', 'w', 'n', 's', 's', 'w', 's', 'e', 's'] walk
Testing a ['w', 'n', 'n', 'w', 'n', 's', 'n', 'n', 'e', 'w'] walk
Testing a ['w', 'n', 'n', 'w', 'n', 's', 'n', 'n', 'e', 'w'] walk
Testing a ['n', 'w', 's', 's', 'n', 'n', 'e', 'n', 'n', 's'] walk
Testing a ['n', 'w', 's', 's', 'n', 'n', 'e', 'n', 's', 's'] walk
Testing a ['w', 'n', 'n', 'w', 'n', 's', 'n', 'n', 'e', 'w'] walk
Testing a ['n', 'w', 's', 's', 'n', 'n', 'e', 'n', 's', 's'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['s', 'w', 'w', 'n', 's', 'w', 'w', 's', 'e', 's'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['s', 's', 'w', 'n', 's', 'w', 'w', 's', 'e', 's'] walk
Testing a ['n', 'w', 's', 's', 'n', 'n', 'e', 'n', 's', 's'] walk
Testing a ['s', 's', 'w', 'n', 's', 'w', 'w', 's', 'e', 's'] walk
Testing a ['w', 'n', 'n', 'w', 'n', 's', 'n', 'e', 'e', 'w'] walk
Testing a ['s', 's', 'w', 'n', 's', 'w', 'w', 's', 'e', 's'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['w', 'n', 'n', 'w', 'n', 's', 'n', 'e', 'n', 'w'] walk
Testing a ['w', 'n', 'n', 'w', 'n', 's', 'n', 'e', 'n', 'w'] walk
Testing a ['s', 's', 'w', 'n', 's', 'w', 'w', 'w', 'e', 's'] walk
Testing a ['s', 's', 'w', 'n', 's', 'w', 'w', 'w', 'e', 's'] walk
Testing a ['s', 's', 'w', 'n', 's', 'w', 'w', 'w', 'e', 'e'] walk
Testing a ['s', 'w', 'e', 'w', 'n', 'e', 'w', 'e'] walk
Testing a ['w', 'e', 'e', 's', 'n', 'w', 'w', 'n'] walk
Testing a ['n', 's', 'e', 's', 'w', 'n', 'w', 'n'] walk
Testing a ['s', 'n', 'n', 'e', 's', 's', 's', 'w'] walk
Testing a ['w', 'n', 's', 'w', 'n', 's', 'n', 'e'] walk
Testing a ['n', 'e', 'w', 'e', 's', 's', 'w', 'e', 'w', 'n'] walk
Testing a ['s', 'w', 's', 'e', 'w', 'n', 'e', 'n', 'w', 'e'] walk
Testing a ['s', 'w', 'w', 'e', 's', 'e', 'e', 'w'] walk
Testing a ['w', 'n', 'n', 's', 'n', 'e', 's', 's', 'n', 's'] walk
Testing a ['w', 'w', 's', 'n', 'e', 'e', 'n', 's'] walk
Testing a ['e', 'w', 'e', 'e', 'w', 'e', 'e', 'w', 'w', 'e'] walk
Testing a ['n', 'w', 'w', 'w', 'e', 'w', 'e', 'e', 'e', 'w'] walk
Testing a ['s', 'e', 's', 'e', 'n', 'w', 'n', 'w'] walk
Testing a ['e', 'e', 'n', 'n', 'n', 'w', 'w', 's', 's', 's'] walk
Testing a ['n', 'n', 'e', 'w', 'n', 'w', 's', 'w', 'e', 's'] walk
Testing a ['s', 'n', 's', 'e', 'n', 's', 'n', 'w'] walk
Testing a ['w', 'n', 'w', 's', 'n', 'e', 's', 'e', 'n', 's'] walk
Testing a ['e', 's', 'n', 'n', 'w', 'n', 's', 's'] walk
Testing a ['s', 'n', 'n', 'n', 's', 's', 's', 's'] walk
Testing a ['e', 'w', 'e', 'w', 'e', 'e', 'e', 'w', 'e', 'w'] walk
Testing a ['w', 'n', 'n', 'w', 'n', 'e', 's', 's', 'e', 's'] walk
Testing a ['s', 's', 'e', 'e', 's', 'n', 'n', 'w', 'w', 'n'] walk
Testing a ['w', 'w', 'e', 'n', 'w', 'e', 'e', 'w', 's', 'e'] walk
Testing a ['w', 'w', 'e', 's', 'n', 'e', 'w', 'n'] walk
Testing a ['n', 'w', 'w', 'e', 's', 'e', 'e', 'w'] walk
Testing a ['n', 'n', 'e', 'w', 's', 's', 'w', 'e'] walk
Testing a ['w', 'e', 'e', 's', 'e', 'w', 'w', 'n'] walk
Testing a ['s', 'n', 'e', 'e', 's', 'n', 's', 'w', 'w', 'n'] walk
Testing a ['e', 'e', 'n', 'n', 'w', 'w', 's', 's'] walk
Testing a ['w', 'w', 'w', 'e', 'w', 'n', 'e', 'e', 'w', 'e'] walk
Testing a ['n', 's', 'e', 'w', 'w', 'n', 'w', 'e'] walk
Testing a ['n', 'w', 's', 'w', 's', 's', 'e', 'n', 'e', 'n'] walk
Testing a ['w', 'e', 'n', 'w', 's', 'n', 'w', 's', 'e', 'n'] walk
Testing a ['w', 'n', 'e', 'e', 'w', 'n', 's', 'w', 'w', 'e'] walk
Testing a ['w', 'n', 'w', 'n', 'e', 's', 'e', 's'] walk
Testing a ['e', 'w', 'e', 's', 'e', 'e', 'w', 'n'] walk
Testing a ['w', 'n', 's', 'n', 'e', 's', 'n', 's'] walk
Testing a ['s', 'e', 's', 'n', 'n', 'n', 'w', 'n', 's', 's'] walk
Testing a ['n', 'e', 's', 's', 'w', 'w', 'n', 'n'] walk
Testing a ['e', 'w', 'w', 's', 'w', 'w', 'e', 'e', 'n', 'e'] walk
Testing a ['e', 'w', 'w', 'n', 's', 'w', 'e', 'e', 's', 'n'] walk
Testing a ['s', 's', 'w', 'e', 's', 'n', 'e', 'w'] walk
Testing a ['s', 's', 's', 'w', 'n', 'n', 'n', 'n', 'e', 's'] walk
Testing a ['e', 'e', 's', 'e', 'w', 'w', 'n', 'w'] walk
Testing a ['e', 'n', 's', 'e', 'e', 's', 'n', 'w'] walk
Testing a ['e', 's', 's', 'n', 'w', 'n', 'n', 's'] walk
Testing a ['e', 'n', 'e', 's', 'e', 's', 'w', 'n'] walk
Testing a ['w', 's', 'w', 'n', 'n', 'n', 'n', 'e', 's', 's'] walk
Testing a ['e', 'w', 'w', 'n', 'w', 'e', 'e', 'e', 's', 'e'] walk
Testing a ['n', 'n', 'e', 'w', 'n', 's', 's', 'w', 'e', 's'] walk
Testing a ['n', 'e', 's', 'w', 's', 'w', 'w', 'n', 'e', 'n'] walk
Testing a ['w', 'w', 'n', 'n', 'n', 'e', 's', 's'] walk
Testing a ['w', 's', 'w', 'e', 's', 'e', 'n', 'e', 'w', 'n'] walk
Testing a ['w', 'e', 's', 's', 'e', 'w', 'n', 'n'] walk
Testing a ['w', 'w', 'w', 'e', 'w', 'e', 'e', 'e', 'w', 'e'] walk
Testing a ['e', 's', 'w', 'e', 'w', 'n', 'e', 'w'] walk
Testing a ['w', 'e', 's', 's', 'n', 'w', 'n', 'n'] walk
Testing a ['e', 'n', 'n', 'e', 'w', 's', 's', 'w'] walk
Testing a ['n', 'n', 'n', 'w', 's', 's', 's', 'e'] walk
Testing a ['s', 'e', 's', 's', 'n', 'w', 'n', 'n'] walk
Testing a ['w', 's', 'e', 'e', 'e', 'e', 'n', 'w', 'w', 'w'] walk
Testing a ['s', 'e', 'e', 'w', 's', 'n', 'w', 'w', 'e', 'n'] walk
Testing a ['e', 'e', 'n', 'n', 'w', 'w', 's', 's'] walk
Testing a ['e', 's', 'e', 'w', 's', 'e', 'n', 'w', 'e', 'n'] walk
Testing a ['n', 'e', 's', 'e', 'e', 's', 'w', 'n', 'w', 'w'] walk
Testing a ['n', 'n', 'w', 'e', 'w', 'w', 's', 'e', 'w', 'e'] walk
Testing a ['n', 's', 'w', 's', 'e', 's', 'n', 'e', 'n', 'w'] walk
Testing a ['e', 's', 'e', 'n', 'e', 'n', 'w', 's'] walk
Testing a ['w', 'n', 'w', 'n', 'w', 'e', 's', 'e', 's', 'e'] walk
Testing a ['n', 'n', 'n', 's', 's', 's', 's', 'n'] walk
Testing a ['w', 's', 'e', 's', 's', 'e', 'n', 'w', 'n', 'n'] walk
Testing a ['n', 's', 'n', 'w', 's', 's', 'n', 's', 'e', 'n'] walk
Testing a ['n', 'w', 'n', 's', 's', 'e', 's', 'n'] walk
Testing a ['w', 's', 'n', 's', 'n', 'e', 'n', 's', 'n', 's'] walk
Testing a ['n', 'w', 'n', 'n', 'e', 's', 'e', 's', 's', 'w'] walk
Testing a ['w', 'e', 'n', 'n', 'e', 'w', 's', 's'] walk
Testing a ['w', 'w', 'n', 'n', 'n', 'e', 's', 's'] walk
Testing a ['e', 'e', 's', 'w', 'w', 'w', 'n', 'e'] walk
Testing a ['s', 'e', 'e', 's', 's', 'w', 'w', 'n'] walk
Testing a ['e', 's', 'w', 'w', 'w', 'n', 'e', 'e'] walk
Testing a ['w', 'e', 's', 'n', 's', 'n', 'w', 'n', 's', 'n'] walk
Testing a ['s', 's', 's', 'e', 's', 'n', 'n', 'w'] walk
Testing a ['e', 'e', 's', 'n', 'e', 'w', 'n', 's'] walk
Testing a ['w', 'n', 's', 's', 'w', 'n', 's', 'n', 'n', 'e'] walk
Testing a ['s', 's', 'n', 'n', 's', 'n', 's', 's'] walk
Testing a ['w', 'e', 'w', 's', 'e', 'w', 'e', 'n'] walk
Testing a ['w', 'e', 'n', 'n', 'n', 'n', 'w', 's', 's', 's'] walk
Testing a ['s', 'w', 'n', 'n', 's', 'e', 's', 's'] walk
Testing a ['w', 'n', 'n', 'n', 'w', 'e', 's', 's', 's', 'e'] walk
Testing a ['e', 'w', 's', 'e', 'n', 'e', 'e', 'n', 'w', 's'] walk
Testing a ['e', 'w', 'n', 'w', 'e', 'e', 'e', 's', 'e', 'w'] walk
Testing a ['n', 'n', 's', 'n', 'w', 'w', 's', 'n', 's', 'e'] walk
Testing a ['s', 's', 's', 'w', 'e', 's', 'n', 'n', 'e', 'w'] walk
Testing a ['n', 'n', 'e', 'e', 's', 's', 'w', 'w'] walk
Testing a ['s', 'w', 'w', 'w', 'n', 'e', 'e', 'e'] walk
Testing a ['s', 'n', 'w', 'w', 'n', 'n', 's', 'e', 'e', 's'] walk
Testing a ['s', 'n', 'w', 's', 's', 'n', 's', 'e', 'n', 'n'] walk
Testing a ['w', 'e', 'e', 's', 's', 'e', 'w', 'w', 'n', 'n'] walk
Testing a ['w', 'w', 'n', 'e', 'e', 'e', 's', 'w'] walk
You have passed all of the tests! :)

