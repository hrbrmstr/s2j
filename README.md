# s2j

A Python utility that reads in Suricata rules and outputs JSON.

## Installation

```bash
$ python3 -m pip install -e git+https://codeberg.org/hrbrmstr/s2j.git#egg=s2j
```

## Usage

```bash
s2j < rules.txt > rules.json
```

Or:

```bash
cat rules.txt | s2j > rules.json
```

Or:

```bash
s2j rules.txt > rules.json
```

### Example

```bash
% curl --silent "https://raw.githubusercontent.com/michalpurzynski/suricata-rules/refs/heads/master/suspicious.rules" | head -1 | s2j | jq
```

Outputs:

```json
[
  {
    "enabled": true,
    "action": "alert",
    "proto": "udp",
    "source_addr": "any",
    "source_port": "any",
    "direction": "->",
    "dest_addr": "any",
    "dest_port": "53",
    "group": null,
    "gid": 1,
    "sid": 2500003,
    "rev": 1,
    "msg": "SURICATA DNS Query to a Suspicious *.ws Domain",
    "flowbits": [],
    "metadata": [],
    "references": [],
    "classtype": null,
    "priority": 0,
    "options": [
      {
        "name": "msg",
        "value": "\"SURICATA DNS Query to a Suspicious *.ws Domain\""
      },
      {
        "name": "content",
        "value": "\"|01 00 00 01 00 00 00 00 00 00|\""
      },
      {
        "name": "depth",
        "value": "10"
      },
      {
        "name": "offset",
        "value": "2"
      },
      {
        "name": "content",
        "value": "\"|02|ws|00|\""
      },
      {
        "name": "nocase",
        "value": null
      },
      {
        "name": "sid",
        "value": "2500003"
      },
      {
        "name": "rev",
        "value": "1"
      }
    ],
    "raw": "alert udp any any -> any 53 (msg:\"SURICATA DNS Query to a Suspicious *.ws Domain\"; content:\"|01 00 00 01 00 00 00 00 00 00|\"; depth:10; offset:2; content:\"|02|ws|00|\"; nocase; sid:2500003; rev:1;)",
    "header": "alert udp any any -> any 53",
    "content": "\"|02|ws|00|\"",
    "depth": "10",
    "offset": "2",
    "nocase": null
  }
]
```
