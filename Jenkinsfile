pipeline{
  agent any
  stages {
  	stage('Build docker image'){
  		steps{
  			script{
  				if (env.BRANCH_ENV != 'master') {
		    		sh 'docker-compose build'
		  		}
				}
    	}
    }
    
    stage('Run containerized application'){
      steps{
  			script{
  				if (env.BRANCH_ENV != 'master' ) {
		    		sh 'docker-compose up '
		  		}
				}
    	}
    }
	  stage('Docker Test Env'){
      steps{
    sh 'python3 -m pip install -r requirements.txt'
      }
    }
		
    stage('Integration and Unit tests '){
     		steps{
     			script{
     				if (env.BRANCH_NAME == 'feature' ) {
							sh 'python3 test_unit.py'
              sh 'python3 test_integration.py'
		    	}
				}
			}
		}
		 stage('stress_test'){
				steps{
					script{
    				if (env.BRANCH_NAME == 'develop') {
      				sh 'python3 test_stress.py'
					}
				}
				
		  }
		}
	
    
		
		
	
		
	
		stage('push to release'){
				steps{
					script{
    				if (env.BRANCH_NAME == 'develop') {
    					sh 'git checkout -b release || git checkout release'	
    					sh 'git fetch'	
    					sh 'git pull'
    					sh 'git merge origin/develop'
    					sh 'git commit --allow-empty -m "release the application"'
    					sh 'git push -f https://Kimpouni:codelyoko_93@github.com/AnasE17/Project-Data-Engineering-2.git'
					}
				}
				
		  }
		}
		
		stage('Release phase'){
     		steps{
     			script{
     				if (env.BRANCH_NAME == 'release') {
							echo '"deploying"' 
		    	}
				}
			}
		}
		
		stage('User acceptance'){
     		steps{
     			script{
     				if (env.BRANCH_NAME == 'release') {
							input 'Accept merge to master ??'
		    	}
				}
			}
		}
		
		stage('Final merging'){
     		steps{
     			script{
     				if (env.BRANCH_NAME == 'release') {
							sh 'git checkout -b main || git checkout main'
							sh 'git merge origin/release'
							sh 'git push -f https://Kimpouni:codelyoko_93@github.com/AnasE17/Project-Data-Engineering-2.git'
		    	}
				}
			}
		}
				
				
		stage('Delete container'){
     		steps{
     			script{
     				if (env.BRANCH_NAME != 'master') {
							sh 'docker-compose down'
		    	}
				}
			}
		}
		
		
	}
}
