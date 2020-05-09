void setup(){
  size(400, 400);
  strokeWeight(5);
}

void draw(){
  background(204);
  line(pmouseX, pmouseY, mouseX, mouseY);
}
