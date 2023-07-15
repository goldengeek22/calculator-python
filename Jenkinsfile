pipeline{
  agent { label 'calculator-python-agent' }
  triggers {
     pollSCM('* * * * *')
  }
  stages {
    stage("Test"){
	steps{
	  sh "/usr/bin/python3 -m unittest discover"
	}
    }
  }
}
