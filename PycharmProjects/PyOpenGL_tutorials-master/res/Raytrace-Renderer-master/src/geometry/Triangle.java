package geometry;

import tools.Epsilon;

/**
 * Represents a triangle in 3D space. <b>NOT COMPLETE!</b>
 * 
 * @author Donny
 *
 */
public class Triangle implements Primitive {
	protected Vector3 v1, v2, v3, n;

	public Triangle(Vector3 p, Vector3 q, Vector3 t) {
		this.v1 = p;
		this.v2 = q;
		this.v3 = t;
		this.n = q.getSubtract(q).cross(t.getSubtract(p));
	}

	public void translate(Vector3 v) {
		v1.add(v);
		v2.add(v);
		v3.add(v);

	}

	public void rotateX(double theta, boolean aroundOrigin) {
		Transform transform = Transform.getRotationXInstance(theta);
		this.v1 = transform.getTransformed(v1);
		this.v2 = transform.getTransformed(v2);
		this.v3 = transform.getTransformed(v3);
	}

	public void rotateY(double theta, boolean aroundOrigin) {
		Transform transform = Transform.getRotationYInstance(theta);
		this.v1 = transform.getTransformed(v1);
		this.v2 = transform.getTransformed(v2);
		this.v3 = transform.getTransformed(v3);
	}

	public void rotateZ(double theta, boolean aroundOrigin) {
		Transform transform = Transform.getRotationZInstance(theta);
		this.v1 = transform.getTransformed(v1);
		this.v2 = transform.getTransformed(v2);
		this.v3 = transform.getTransformed(v3);
	}

	public boolean contains(Vector3 v) {
		return false;
	}

	public Intersection intersects(Ray r) {
		System.out.println("r: "+r);
		System.out.println("v1: "+v1);
		System.out.println("v2: "+v2);
		System.out.println("v3: "+v3);
		
		Vector3 e1 = v2.clone().sub(v1);
		Vector3 e2 = v3.clone().sub(v1);
		
		System.out.println("e1: "+e1+" v2 - v1");
		System.out.println("e2: "+e2+" v3 - v1");
		Vector3 p = r.getDir().cross(e2);
		System.out.println("pvec: "+p+" d x e2");
		double det = e1.dot(p);
		
		System.out.println("det: "+det+" e1 * p");
		if (Epsilon.nearlyEquals(det, 0.0))
			return new Intersection();

		double invDet = 1.0 / det;
		
		System.out.println("invDet: "+ invDet+ "1/det");
		
		Vector3 t = r.getOrigin().clone().sub(v1);

		System.out.println("tvec: "+t+" o - v1");
		
		double u = t.dot(p) * invDet;
		
		System.out.println("u: "+u+" (t * p)*invDet");
		if (u < 0.0 || u > 1.0)
			return new Intersection();
		Vector3 q = t.cross(e1);
		
		System.out.println("q: "+q+"t x e1");
		double v = r.getDir().dot(q) * invDet;
		
		System.out.println("v: "+v+" (d * q) * invDet");
		if (v < 0.0 || v > 1.0)
			return new Intersection();
		double T = e2.dot(q) * invDet;
		
		System.out.println("T: "+T+" (e1 * q) * invDet");
		if (T < 0.0)
			return new Intersection();

		return new Intersection(true, r.pointOnRay(T), n);
	}

	public Vector3 getNormal(Vector3 p) {
		return n;
	}

	public Primitive clone() {
		return new Triangle(v1.clone(), v2.clone(), v3.clone());
	}

	public boolean equals(Primitive prim) {
		if (prim instanceof Triangle) {
			return true;
			// too lazy to write this code
		}
		return false;
	}

}
