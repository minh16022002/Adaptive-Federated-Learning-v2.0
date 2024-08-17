from util.time_generation import TimeGeneration
import os

SERVER_ADDR = 'localhost'   # When running in a real distributed setting, change to the server's IP address
SERVER_PORT = 51000

dataset_file_path = os.path.join(os.path.dirname(__file__), 'datasets')
results_file_path = os.path.join(os.path.dirname(__file__), 'results')
single_run_results_file_path = results_file_path + '/SingleRun.csv'
multi_run_results_file_path = results_file_path + '/MultipleRuns.csv'

# Model, dataset, and control parameter configurations for MNIST with SVM
# dataset = 'MNIST_ORIG_EVEN_ODD'  # Use for SVM model
# model_name = 'ModelSVMSmooth'
# control_param_phi = 0.025   # Good for MNIST with smooth SVM

# Model, dataset, and control parameter configurations for MNIST with CNN
dataset = 'MNIST_ORIG_ALL_LABELS'  # Use for CNN model
model_name = 'ModelCNNMnist'
control_param_phi = 0.00005   # Good for CNN

# Model, dataset, and control parameter configurations for CIFAR-10 with CNN
# dataset = 'CIFAR_10'
# model_name = 'ModelCNNCifar10'
# control_param_phi = 0.00005   # Good for CNN

n_nodes = 5  # Specifies the total number of clients

moving_average_holding_param = 0.0  # Moving average coefficient to smooth the estimation of beta, delta, and rho

step_size = 0.01

# Setting batch_size equal to total_data makes the system use deterministic gradient descent;
# Setting batch_size equal < total_data makes the system use stochastic gradient descent.
# batch_size = 1000  # Value for deterministic gradient descent
# total_data = 1000  # Value for deterministic gradient descent
batch_size = 100  # 100  # Value for stochastic gradient descent
total_data = 60000  # 60000  #Value for stochastic gradient descent

# Choose whether to run a single instance and plot the instantaneous results or
# run multiple instances and plot average results
single_run = False

# Choose whether to estimate beta and delta in all runs, including those where tau is not adaptive,
# this is useful for getting statistics. NOTE: Enabling this may change the communication time when using
# real-world measurements for resource consumption
estimate_beta_delta_in_all_runs = False

# If true, the weight corresponding to minimum loss (the loss is estimated if using stochastic gradient descent) is
# returned. If false, the weight at the end is returned. Setting use_min_loss = True corresponds to the latest
# theoretical bound for the **DISTRIBUTED** case.
# For the **CENTRALIZED** case, set use_min_loss = False,
# because convergence of the final value can be guaranteed in the centralized case.
use_min_loss = True

# Specifies the number of iterations the client uses the same minibatch, using the same minibatch can reduce
# the processing time at the client, but may cause a worse model accuracy.
# We use the same minibatch only when the client receives tau_config = 1
num_iterations_with_same_minibatch_for_tau_equals_one = 3

# Specifies whether all the data should be read when using stochastic gradient descent.
# Reading all the data requires much more memory but should avoid slowing down due to file reading.
read_all_data_for_stochastic = True

MAX_CASE = 4  # Specifies the maximum number of cases, this should be a constant equal to 4
tau_max = 100  # Specifies the maximum value of tau

# tau_setup = -1 is for the proposed adaptive control algorithm, other values of tau correspond to fixed tau values
if not single_run:
    tau_setup_all = [-1, 1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100]
    sim_runs = range(0, 2)  # Specifies the simulation seeds in each simulation round
    case_range = range(0, MAX_CASE)
else:
    case_range = [0]   # Change if we want single run with other case, should only have one case
    tau_setup_all = [-1]   # Should only have one value
    sim_runs = [0]   # Should only have one value, the value specifies the random seed


max_time = 15  # Total time budget in seconds

# If time_gen is None, use actual measured time. Else, use time generated by the TimeGeneration class.
time_gen = None
# time_gen = TimeGeneration(1, 0.0, 1e-10, 0.0, 0.0, 0.0)

multiply_global = 1.0
multiply_local = 1.0

# These numbers are from measurement on stochastic gradient descent on SVM smooth with MNIST even/odd data.
# time_gen = TimeGeneration(multiply_local * 0.013015156, multiply_local * 0.006946299, 1e-10,
#                           multiply_global * 0.131604348, multiply_global * 0.053873234, 1e-10)

# These numbers are from measurement on CENTRALIZED stochastic gradient descent on SVM smooth with MNIST even/odd data.
# time_gen = TimeGeneration(multiply_local * 0.009974248, multiply_local * 0.011922926, 1e-10,
#                           0.0, 0.0, 0.0)

# These numbers are from measurement on deterministic gradient descent on SVM smooth with MNIST even/odd data.
# time_gen = []
# time_gen.append(TimeGeneration(multiply_local * 0.020613052, multiply_local * 0.008154439, 1e-10,
#                                multiply_global * 0.137093837, multiply_global * 0.05548447, 1e-10))  # Case 1
# time_gen.append(TimeGeneration(multiply_local * 0.021810727, multiply_local * 0.008042984, 1e-10,
#                                multiply_global * 0.12322071, multiply_global * 0.048079171, 1e-10))  # Case 2
# time_gen.append(TimeGeneration(multiply_local * 0.095353094, multiply_local * 0.016688657, 1e-10,
#                                multiply_global * 0.157255906, multiply_global * 0.066722225, 1e-10))  # Case 3
# time_gen.append(TimeGeneration(multiply_local * 0.022075891, multiply_local * 0.008528005, 1e-10,
#                                multiply_global * 0.108598094, multiply_global * 0.044627335, 1e-10))  # Case 4
