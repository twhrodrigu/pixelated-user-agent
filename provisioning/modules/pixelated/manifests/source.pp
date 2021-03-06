class pixelated::source {
  include phantomjs

  package { [
    'git',
    'nodejs-legacy',
    'python-dev',
    'python-virtualenv',
    'libffi-dev',
    'g++',
    'ruby-dev',
    'libsqlite3-dev',
    'libfontconfig1']:
    ensure => latest
  }

  include pixelated::source::npm

  package { 'compass':
    ensure   => installed,
    provider => 'gem'
  }

  stage { 'install_pixelated': }

  class { 'pixelated::source::install_useragent' :
    stage => install_pixelated
  }

  Stage['main'] -> Stage['install_pixelated']
}
