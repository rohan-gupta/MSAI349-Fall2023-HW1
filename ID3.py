from node import Node
import math
import json

def ID3(examples, default):
  '''
  Takes in an array of examples, and returns a tree (an instance of Node) 
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"
  '''
  root = ptr = Node()

  if is_dataset_empty(examples):
    return root

  if is_dataset_positive(examples):
    ptr.label = "+"
    return root

  if is_dataset_negative(examples):
    ptr.label = "-"
    return root

  attributes = get_all_attributes(examples)
  best_attribute = ""
  best_attribute_information_gain = 0

  for a in attributes:
    temp = get_information_gain(dataset, a)
    if temp > best_attribute_information_gain:
      best_attribute = a
      best_attribute_information_gain = temp

  # split dataset

  # create child nodes

  # repeat process for each child node

  return root

def prune(node, examples):
  '''
  Takes in a trained tree and a validation set of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  '''

def test(node, examples):
  '''
  Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
  of examples the tree classifies correctly).
  '''


def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''

def is_dataset_empty(dataset):
  pass

def is_dataset_positive(dataset):
  pass

def is_dataset_negative(dataset):
  pass

def get_all_attributes(dataset):
  all_attributes = set()

  for d in dataset:
    for k in d:
      if k == "Class":
        continue
      
      all_attributes.add(k)

  return list(all_attributes)

def get_information_gain(dataset, attribute):
  sub_dataset = get_sub_datasets_by_attribute(dataset, attribute)
  parent_entropy = get_entropy(dataset)
  child_entropy = 0

  for s in sub_dataset:
    child_entropy += (len(s) / len(dataset)) * get_entropy(s)
  
  return parent_entropy - child_entropy
  

def get_sub_datasets_by_attribute(dataset, attribute):
  sub_datasets = {}

  for d in dataset:
    if attribute not in d:
      continue

    if d[attribute] not in sub_dataset:
      sub_datasets[d[attribute]] = []

    sub_datasets[d[attribute]].append(d)

  return list(sub_datasets.values())


def get_entropy(dataset):
  target_class_probability = get_target_class_probability(dataset)
  H = 0

  for k, v in target_class_probability.items():
    H += -1 * v * math.log2(v)

  return H


def get_target_class_frequencies(dataset):
  target_class_frequencies = {}
  
  for d in dataset:
    for k, v in d.items():
      if k != "Class":
        continue

      if v not in target_class_frequencies:
        target_class_frequencies[v] = 0

      target_class_frequencies[v] += 1

  return target_class_frequencies


def get_target_class_probabilities(dataset):
  target_class_frequencies = target_class_frequencies(dataset)
  probabilities = {}

  for k, v in target_class_frequencies.items():
    probabilities[k] = v / len(dataset)

  return probabilities
