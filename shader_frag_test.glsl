#version 330 core

uniform sampler2D tex;
uniform float time;

in vec2 uvs;
out vec4 f_color;

float blue_variation(in float blue_v, in float pos, in float time){
    return mix(0., 1., sin(time*0.1 + pos)/2 + 0.5);
}

void main() {
    vec3 sampled_col = texture(tex, uvs).rgb;
    float blue = blue_variation(sampled_col.b, uvs.x, time/10);
    f_color = vec4(sampled_col.rg, blue,  1.0);
}