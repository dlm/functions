# Cape Functions

## Getting Started

To run these functions with Cape, you need to first install the [Cape CLI](https://github.com/capeprivacy/cli).

### Cape Login

Log in to Cape by running:
```
cape login
```

### Cape Deploy

Deploys your function and any dependencies within a `function_dir` to Cape. Returns a `function_id`:

```
cape deploy <function_dir>
```

For example, if your function code was within a folder named `echo`:
```
cape deploy echo
```

#### Deploying on Windows

If you are on Windows (or as an alternative to deploying the function as a directory) you can create a zip file and deploy it directly. This will fix issues you may run into with relative paths:

```
cape deploy <function_name>.zip
```

### Cape Run

Runs a cape function by `function_id` and takes `input_data`. Returns the result of the function:

```
cape run <function_id> <input_data>
```

to pass `input_data` as a file, use `-f`:
```
cape run <function_id> -f <input_file>
```


## Examples

### echo

A simple function that returns whatever you send it.

```
cape deploy echo
```

```
cape run <YOUR_FUNCTION_ID> -f input.echo.data
```

### isprime

```
cape deploy isprime
```

```
cape run <YOUR_FUNCTION_ID> -f input.isprime.data
```

### pendulum
In this example, we show how to run a function requiring a dependency. The function simply returns the current time based on a specific timezone using the [Pendulum](https://pendulum.eustace.io/) library. To learn how to deploy this function, checkout the folder [pendulum](./pendulum/). To invoke the function, invoke:

```
cape run capedocs/pendulum Europe/Paris 
```

### np-stats
A simple example with numpy dependencies and using [pycape](https://github.com/capeprivacy/pycape) and [serdio.lift_io](https://pydocs.capeprivacy.com/serdio.io_lifter.html#serdio.io_lifter.lift_io) to handle automatic serialization/deserialization of Cape function input/outputs. You can learn how to deploy this function by checking the folder [np-stats](./np-stats/). You can run the function as follow after install installing in a virtual environment in `np-stats/requirements.txt`:

```
export TOKEN=<YOUR TOKEN>
export FUNCTION_ID=capedocs/np-stats
python np-stats/run.py
```

### secure_search
Simulates a cybersecurity search function, where the IP addresses you are interested in need to remain private but the data/logs you are searching might be public. You can learn more about this function by checking the folder [secure-search](./secure_search/).

```
cape run capedocs/secure-search -f secure-search/input.search.data
```

### leader_election
Demos how secure trusted execution environment like Cape can be leveraged in consensus in order to guarantee fairness. Details on how to run this example can be found
[here](https://github.com/capeprivacy/functions/tree/main/leader-election)