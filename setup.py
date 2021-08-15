from distutils.core import setup
setup(
  name = 'ILib',         
  packages = ['ILib'],   
  version = '0.4',     
  description = 'Image processing library using opencv and mediapipe',  
  author = 'Vansh Kachhwal',                   
  author_email = 'kachhwalvansh230@gmail.com',      
  url = 'https://github.com/VanshKachhwal',   
  download_url = 'https://github.com/VanshKachhwal/ILib/archive/refs/tags/0.4.tar.gz',    
  keywords = ['PoseDetector', 'AutoAligner', 'BackgroundRemover', 'MosaicMaker', 'CollageMaker'],   # Keywords that define your package best
  install_requires=[            
          'opencv-contrib-python',
          'mediapipe',
          'numpy'
      ],
  classifiers=[
    'Intended Audience :: Education',      
    'Topic :: Image Processing :: Utilities',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.6',      
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
