# Golang

Master: [![Build Status](https://travis-ci.org/sansible/golang.svg?branch=master)](https://travis-ci.org/sansible/golang)  
Develop: [![Build Status](https://travis-ci.org/sansible/golang.svg?branch=develop)](https://travis-ci.org/sansible/golang)

* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This roles installs Golang.


## Installation and Dependencies

To install run `ansible-galaxy install sansible.golang` or add this to your
`roles.yml`.

```YAML
- name: sansible.golang
  version: v2.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`


## Tags

This role uses one tag: **build** 

* `build` - Installs Golang and all its dependencies.


## Examples

To install:

```YAML
- name: Install and configure Golang
  hosts: "somehost"

  roles:
    - role: sansible.golang
```

Setup Golang workspace for a user:

```YAML
- name: Install and configure Golang
  hosts: "somehost"

  roles:
    - role: sansible.golang
      sansible_golang_workspace_user: api_user
```
