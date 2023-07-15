pipeline{
  agent { label 'calculator-python-agent' }
  triggers {
     pollSCM('* * * * *')
  }
  stages {
    stage("Test"){
	steps{
	  sh "python3 -m unittest discover"
	}
    }
  }
}
