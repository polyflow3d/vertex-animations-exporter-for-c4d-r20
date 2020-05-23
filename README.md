 
# Vertex Animations Exporter for 3DS MAX

 an scripted (MaxScript) exporter of 
 * .obj files sequences 
 * Point Caches (.pc2) 
 

 designed for  [Vertex Animation Tools](http://u3d.as/1iJP)  

## Installation
 
 <details style=" background-color:white; padding-left: 10px; margin-left: 10px; margin-right: 60px;" >
  <summary>  run maxscript file <i>vertex-animations-exporter-3dsmax.ms</i>  </summary>

 ![alt text](https://polyflow.xyz/content/vertex-animation-tools/vertex-animations-exporter-3dsmax/vertex-animations-exporter-3dsmax-runscript-gif.gif)

</details>

## Compatibility
* 3ds MAX 2010 or newer


## Usage

### to export .obj sequence
* select output files
* select object to export
* press _Export Mesh Sequence_

### to export Point Cache  
* select output .pc2 and .obj files
* select object to export
* press _Export Point Cache_

## Which export type should be used?

* If animated object are changes its topology or vertex count during animation use **Mesh Sequence**  
    * animation of construction
    * demolition
    * shatter
    * fluid simulations
    * cross sections

* If animated object *not* changes its topology or vertex count during animation use **Mesh Sequence** or **Point Cache**. 
    * cloth simulations 
    * deformations 
    * skinned mesh animations 
 

 

## License
[MIT](https://choosealicense.com/licenses/mit/)