#version 330 core

uniform sampler2D tex_image;
uniform sampler2D tex_noise;
// uniform float time;
// uniform int screen_width;

in vec2 uvs;
out vec4 f_color;

float average(in vec3 v3){
    return (v3.r + v3.g + v3.b)/3;
}

void main() {
    // float y = mod(uvs.y + time/10, screen_width);
    vec3 sampled_image = texture(tex_image, uvs).rgb;
    vec3 sampled_noise = texture(tex_noise, vec2(uvs.x, uvs.y)).rgb;
    float avg_image = average(sampled_image);
    float avg_noise = average(sampled_noise);
    float new_val;
    float d;

    d = step(avg_noise+0.4, avg_image);
    new_val = d*avg_image;
    new_val += (1-d)*0.4;
    d = step(avg_noise, avg_image);
    new_val = d*new_val;
    new_val *= d;
    d = step(avg_noise+0.4, avg_image);
    new_val = (1-d)*new_val + d;
    f_color = vec4(vec3(new_val),  1.0);
}