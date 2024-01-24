# kill process killmenow

exec { 'pkill':
  command  => 'pkill killmenow',
  path => '/bin:/usr/bin',
  provider => 'shell',
  refreshonly => true,
}
