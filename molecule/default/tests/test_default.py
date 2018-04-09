import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_users(host):
    assert host.user('go').group == 'go'


def test_directories(host):
    directories = [
        '/home/go/go/bin/', '/home/go/go/pkg/', '/home/go/go/src/',
        '/home/go/go/src/github.com',
    ]
    for dir in directories:
        host.file(dir).is_directory


def test_go_version(host):
    go_version = host.check_output('/usr/local/go/bin/go version')
    assert go_version == 'go version go1.6 linux/amd64'
