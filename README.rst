gron
========================================

python version of https://github.com/tomnomnom/gron


examples
----------------------------------------

input file

.. code-block:: javascript

  {
    "one": 1,
    "two": 2.2,
    "three-b": "3",
    "four": [1,2,3,4],
    "five": {
      "alpha": ["fo", "fum"],
      "beta": {
        "hey": "How's tricks?"
      }
    },
    "abool": true,
    "abool2": false,
    "isnull": null,
    "id": 66912849
  }

code

.. code-block:: python

  import gron
  with open("<file.json>") as rf:
      data = json.load(rf)
  print("\n".join(gron.gron(data)))

output

::

  json = {};
  json.abool = true;
  json.abool2 = false;
  json.five = {};
  json.five.alpha = [];
  json.five.alpha[0] = "fo";
  json.five.alpha[1] = "fum";
  json.five.beta = {};
  json.five.beta.hey = "How's tricks?";
  json.four = [];
  json.four[0] = 1;
  json.four[1] = 2;
  json.four[2] = 3;
  json.four[3] = 4;
  json.id = 66912849;
  json.isnull = null;
  json.one = 1;
  json["three-b"] = "3";
  json.two = 2.2;

