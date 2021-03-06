# Q.30. Can you explain the life cycle of a thread?
#
#
# python scripting interview questions
#
# To create a thread, we create a class that we make override the run method
# of the thread class. Then, we instantiate it.
# A thread that we just created is in the new state. When we make a call to
# start() on it, it forwards the threads for scheduling. These are in the
# ready state.
# When execution begins, the thread is in the running state.
# Calls to methods like sleep() and join() make a thread wait. Such a thread
# is in the waiting/blocked state.
# When a thread is done waiting or executing, other waiting threads are sent
# for scheduling.
# A running thread that is done executing terminates and is in the dead state.
# Basic Python Program Interview Questions and Answers