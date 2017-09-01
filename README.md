# Edition Comparison

Given several lists of software that coming from different agents, and each agent has one list. One list differ from each other. We need to generate a 2D table, where the first dimension is software list, and the other is device list, moreover, the value of this table is a software information of given software on the given device.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Temporarily, this tool doesn't need any extra module but the python standard.

### Installing

TODO

## Data Structure

A demo data is provided in the 'data' subfolder, which is a concatenated version of five lists coming from five build agents.

### Input Data Structure


```
[
    'device1':'microsoft visual c++ 2015 redistributable (x64) 14.0.24215',
    'device1':'Microsoft Visual Studio 2015 XAML Application Timeline',
    'device2':'microsoft visual c++ 2013 x86 minimum runtime - 11.0.60610',
    'device3':'WCF Data Services 5.6.4 Runtime,1.50423E+12',
    'device4':'Visual C++ IDE Common Package'
]
```

### Output Data Structure

```
{
    'software1':{
        'device1':{
            'has' : True,
            'version': '1.2.3.1',
            'suffix' : 'ENV'
        },
        'device2':{
            'has' : False,
            'version' : '13.4.0'
            'suffix' : ''
        }
        'device3':{
            'has' : False,
            'version' : '13.4.0'
            'suffix' : ''
        }
        'device4':{
            'has' : False,
            'version' : '13.4.0'
            'suffix' : ''
        }
    },
    'software2':{
        'device1':{
            'has' : True,
            'version': '1.2.3.1',
            'suffix' : 'ENV'
        },
        'device2':{
            'has' : True,
            'version' : '4.0'
            'suffix' : ''
        }
        'device3':{
            'has' : False,
            'version' : ''
            'suffix' : ''
        }
        'device4':{
            'has' : False,
            'version' : ''
            'suffix' : ''
        }
    },
    'software3':{
        'device1':{
            'has' : False,
            'version': '',
            'suffix' : ''
        },
        'device2':{
            'has' : False,
            'version' : ''
            'suffix' : ''
        }
        'device3':{
            'has' : False,
            'version' : ''
            'suffix' : ''
        }
        'device4':{
            'has' : False,
            'version' : ''
            'suffix' : ''
        }
    },
    'software4':{
        'device1':{
            'has' : True,
            'version': '1.2.1',
            'suffix' : 'ENV'
        },
        'device2':{
            'has' : True,
            'version' : '3.0'
            'suffix' : ''
        }
        'device3':{
            'has' : True,
            'version' : '1.0'
            'suffix' : ''
        }
        'device4':{
            'has' : True,
            'version' : '1.0'
            'suffix' : ''
        }
    },
}
```

```
Give an example
```

## Deployment

TODO

## Built With

TODO

## Contributing

TODO

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **QIAO Tian** - *Initial work*

## License

Do what the fuck you want to do with this code. Cause, I guess you are in trouble if you read this line.

Good luck!

## Acknowledgments

* CCTV
* Donald Trump
* San Pang
