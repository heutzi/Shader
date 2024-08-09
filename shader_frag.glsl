#version 330 core

uniform sampler2D tex_image;
uniform sampler2D tex_noise;
uniform float time;

in vec2 uvs;
out vec4 f_color;

float average(in vec3 v3){
    return (v3.r + v3.g + v3.b)/3;
}

void main() {
    vec3 sampled_image = texture(tex_image, uvs).rgb;
    vec3 sampled_noise = texture(tex_noise, uvs).rgb;
    float avg_image = average(sampled_image);
    float avg_noise = average(sampled_noise);
    float d = step(avg_noise, avg_image);
    avg_image *= d;
    f_color = vec4(vec3(avg_image),  1.0);
}