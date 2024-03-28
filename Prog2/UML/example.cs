class Particle
{
    public Vector2 Position;
    public Vector2 Speed;
    public int ImageOffsetX;
    public int ImageOffsetY;
}

class GameObject {
    public bool isDead;
    public Vector2 Position;
    public float Radius;
    public Vector2 Speed;
    public float Rotation;

    public bool CollidesWith(IGameObject other){
        // Code for collision detection
    };
}


class Meteor : GameObject {
    public MeterType Type;
    public float ExplosionScale;
    public float ExplosionScale;

    public void Meter(MeteorType type){
        // Code for meter function
    }

    public void Update(GameTime gameTime){
        // Code for update function
    }

    public IEnumerable<Meteor> BreakMeteor(Meteor meteor){
        // Code for break meteor function
    }
}