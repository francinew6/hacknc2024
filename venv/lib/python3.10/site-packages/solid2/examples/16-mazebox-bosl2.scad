include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/version.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/constants.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/transforms.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/distributors.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/mutators.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/color.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/attachments.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/shapes3d.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/shapes2d.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/drawing.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/masks3d.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/masks2d.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/math.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/paths.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/lists.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/comparisons.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/linalg.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/trigonometry.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/vectors.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/affine.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/coords.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/geometry.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/regions.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/strings.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/skin.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/vnf.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/utility.scad>;
include </home/jeff/code/solid_stuff/SolidPython/solid2/extensions/bosl2/BOSL2/partitions.scad>;

difference() {
	union() {
		tube(or = 30.357749073643905, center = true, h = 88, ir = 28.357749073643905);
		down(z = 40) {
			zcyl(h = 10, r = 35.557749073643905);
		}
	}
	union() {
		cylindrical_extrude(or = 30.557749073643905, ir = 30.357749073643905) {
			offset(r = 0.0) {
				projection(cut = true) {
					up(z = 10) {
						surface(center = true, file = "maze7.png", invert = true);
					}
				}
			}
		}
		cylindrical_extrude(or = 30.357749073643905, ir = 30.157749073643906) {
			offset(r = -0.01231165940486223) {
				projection(cut = true) {
					up(z = 10) {
						surface(center = true, file = "maze7.png", invert = true);
					}
				}
			}
		}
		cylindrical_extrude(or = 30.157749073643906, ir = 29.957749073643903) {
			offset(r = -0.04894348370484647) {
				projection(cut = true) {
					up(z = 10) {
						surface(center = true, file = "maze7.png", invert = true);
					}
				}
			}
		}
		cylindrical_extrude(or = 29.957749073643903, ir = 29.757749073643904) {
			offset(r = -0.1089934758116321) {
				projection(cut = true) {
					up(z = 10) {
						surface(center = true, file = "maze7.png", invert = true);
					}
				}
			}
		}
		cylindrical_extrude(or = 29.757749073643904, ir = 29.557749073643905) {
			offset(r = -0.19098300562505255) {
				projection(cut = true) {
					up(z = 10) {
						surface(center = true, file = "maze7.png", invert = true);
					}
				}
			}
		}
		cylindrical_extrude(or = 29.557749073643905, ir = 29.357749073643905) {
			offset(r = -0.2928932188134524) {
				projection(cut = true) {
					up(z = 10) {
						surface(center = true, file = "maze7.png", invert = true);
					}
				}
			}
		}
		cylindrical_extrude(or = 29.357749073643905, ir = 29.157749073643906) {
			offset(r = -0.41221474770752686) {
				projection(cut = true) {
					up(z = 10) {
						surface(center = true, file = "maze7.png", invert = true);
					}
				}
			}
		}
		cylindrical_extrude(or = 29.157749073643906, ir = 28.957749073643903) {
			offset(r = -0.5460095002604533) {
				projection(cut = true) {
					up(z = 10) {
						surface(center = true, file = "maze7.png", invert = true);
					}
				}
			}
		}
		cylindrical_extrude(or = 28.957749073643903, ir = 28.757749073643904) {
			offset(r = -0.6909830056250525) {
				projection(cut = true) {
					up(z = 10) {
						surface(center = true, file = "maze7.png", invert = true);
					}
				}
			}
		}
		cylindrical_extrude(or = 28.757749073643904, ir = 28.557749073643905) {
			offset(r = -0.843565534959769) {
				projection(cut = true) {
					up(z = 10) {
						surface(center = true, file = "maze7.png", invert = true);
					}
				}
			}
		}
		zrot(a = 120.0) {
			union() {
				cylindrical_extrude(or = 30.557749073643905, ir = 30.357749073643905) {
					offset(r = 0.0) {
						projection(cut = true) {
							up(z = 10) {
								surface(center = true, file = "maze7.png", invert = true);
							}
						}
					}
				}
				cylindrical_extrude(or = 30.357749073643905, ir = 30.157749073643906) {
					offset(r = -0.01231165940486223) {
						projection(cut = true) {
							up(z = 10) {
								surface(center = true, file = "maze7.png", invert = true);
							}
						}
					}
				}
				cylindrical_extrude(or = 30.157749073643906, ir = 29.957749073643903) {
					offset(r = -0.04894348370484647) {
						projection(cut = true) {
							up(z = 10) {
								surface(center = true, file = "maze7.png", invert = true);
							}
						}
					}
				}
				cylindrical_extrude(or = 29.957749073643903, ir = 29.757749073643904) {
					offset(r = -0.1089934758116321) {
						projection(cut = true) {
							up(z = 10) {
								surface(center = true, file = "maze7.png", invert = true);
							}
						}
					}
				}
				cylindrical_extrude(or = 29.757749073643904, ir = 29.557749073643905) {
					offset(r = -0.19098300562505255) {
						projection(cut = true) {
							up(z = 10) {
								surface(center = true, file = "maze7.png", invert = true);
							}
						}
					}
				}
				cylindrical_extrude(or = 29.557749073643905, ir = 29.357749073643905) {
					offset(r = -0.2928932188134524) {
						projection(cut = true) {
							up(z = 10) {
								surface(center = true, file = "maze7.png", invert = true);
							}
						}
					}
				}
				cylindrical_extrude(or = 29.357749073643905, ir = 29.157749073643906) {
					offset(r = -0.41221474770752686) {
						projection(cut = true) {
							up(z = 10) {
								surface(center = true, file = "maze7.png", invert = true);
							}
						}
					}
				}
				cylindrical_extrude(or = 29.157749073643906, ir = 28.957749073643903) {
					offset(r = -0.5460095002604533) {
						projection(cut = true) {
							up(z = 10) {
								surface(center = true, file = "maze7.png", invert = true);
							}
						}
					}
				}
				cylindrical_extrude(or = 28.957749073643903, ir = 28.757749073643904) {
					offset(r = -0.6909830056250525) {
						projection(cut = true) {
							up(z = 10) {
								surface(center = true, file = "maze7.png", invert = true);
							}
						}
					}
				}
				cylindrical_extrude(or = 28.757749073643904, ir = 28.557749073643905) {
					offset(r = -0.843565534959769) {
						projection(cut = true) {
							up(z = 10) {
								surface(center = true, file = "maze7.png", invert = true);
							}
						}
					}
				}
			}
		}
		zrot(a = 240.0) {
			union() {
				cylindrical_extrude(or = 30.557749073643905, ir = 30.357749073643905) {
					offset(r = 0.0) {
						projection(cut = true) {
							up(z = 10) {
								surface(center = true, file = "maze7.png", invert = true);
							}
						}
					}
				}
				cylindrical_extrude(or = 30.357749073643905, ir = 30.157749073643906) {
					offset(r = -0.01231165940486223) {
						projection(cut = true) {
							up(z = 10) {
								surface(center = true, file = "maze7.png", invert = true);
							}
						}
					}
				}
				cylindrical_extrude(or = 30.157749073643906, ir = 29.957749073643903) {
					offset(r = -0.04894348370484647) {
						projection(cut = true) {
							up(z = 10) {
								surface(center = true, file = "maze7.png", invert = true);
							}
						}
					}
				}
				cylindrical_extrude(or = 29.957749073643903, ir = 29.757749073643904) {
					offset(r = -0.1089934758116321) {
						projection(cut = true) {
							up(z = 10) {
								surface(center = true, file = "maze7.png", invert = true);
							}
						}
					}
				}
				cylindrical_extrude(or = 29.757749073643904, ir = 29.557749073643905) {
					offset(r = -0.19098300562505255) {
						projection(cut = true) {
							up(z = 10) {
								surface(center = true, file = "maze7.png", invert = true);
							}
						}
					}
				}
				cylindrical_extrude(or = 29.557749073643905, ir = 29.357749073643905) {
					offset(r = -0.2928932188134524) {
						projection(cut = true) {
							up(z = 10) {
								surface(center = true, file = "maze7.png", invert = true);
							}
						}
					}
				}
				cylindrical_extrude(or = 29.357749073643905, ir = 29.157749073643906) {
					offset(r = -0.41221474770752686) {
						projection(cut = true) {
							up(z = 10) {
								surface(center = true, file = "maze7.png", invert = true);
							}
						}
					}
				}
				cylindrical_extrude(or = 29.157749073643906, ir = 28.957749073643903) {
					offset(r = -0.5460095002604533) {
						projection(cut = true) {
							up(z = 10) {
								surface(center = true, file = "maze7.png", invert = true);
							}
						}
					}
				}
				cylindrical_extrude(or = 28.957749073643903, ir = 28.757749073643904) {
					offset(r = -0.6909830056250525) {
						projection(cut = true) {
							up(z = 10) {
								surface(center = true, file = "maze7.png", invert = true);
							}
						}
					}
				}
				cylindrical_extrude(or = 28.757749073643904, ir = 28.557749073643905) {
					offset(r = -0.843565534959769) {
						projection(cut = true) {
							up(z = 10) {
								surface(center = true, file = "maze7.png", invert = true);
							}
						}
					}
				}
			}
		}
	}
}
