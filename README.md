https://chaquo.com/chaquopy/doc/current/android.html

B1: add classpath :
  buildscript {
      repositories {
         ...
          maven { url "https://chaquo.com/maven" }
      }
     dependencies {
          ...
          classpath "com.chaquo.python:gradle:10.0.1"
      }
  }
 
B2 : add id plugin: 
  plugins {
          id 'com.android.application'
          id 'com.chaquo.python'
          }
 
B3: set path python in pc to build python : 
    defaultConfig {
      python {
         buildPython "C:/path/to/python.exe"
      }
     }
     
B4: set path of python file (source code):
      android {
         sourceSets {
            main {
              python.srcDir "some/other/dir"
            }
          }
      }
 
B5: import libs 
*note: garduate version of Chaquopy version,  Android Gradle plugin and Minimum Android API level is comparible

  defaultConfig {
     python {
         pip {
             install "numpy"
         }
      }
  }
  
B6: set up ABI selection :
defaultConfig {
    ndk {
       abiFilters "armeabi-v7a", "arm64-v8a", "x86", "x86_64"
    }
}
