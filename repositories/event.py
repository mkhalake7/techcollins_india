""" Defines the Event repository """
from datetime import datetime, date, time, timedelta
from models import db
from models.event import Event
from flask import abort


class EventRepository:
    """ The repository for the event model """

    @staticmethod
    def get(key):
        """ Query an event by id or name """
        try:
            res = Event.query.filter(Event.name == key).one_or_none()
            if res:
                return res
            res_id = {}
            if key.isdigit():
                res_id = Event.query.get(int(key))
            return res_id
        except Exception as e:
            print(e)
            abort(400, {'message': 'Invalid value'})

    @staticmethod
    def list():
        """ List all the events """
        return Event.query.all()

    @staticmethod
    def post(data):
        """ Create an event """
        try:
            data['date'] = datetime.strptime(data['date'], '%a, %d %b %Y %H:%M:%S %Z').date()

            # Convert start_time
            try:
                data['start_time'] = datetime.strptime(data['start_time'], '%H:%M:%S').time()
            except:
                data['start_time'] = datetime.strptime(data['start_time'], '%H:%M').time()

            # Convert end_time (if it's in seconds since midnight)
            data['end_time'] = (datetime.min + timedelta(seconds=data['end_time'])).time()
            event = Event(
                name=data['name'],
                date=data['date'],
                start_time=data['start_time'],
                end_time=data['end_time'],
                venue=data['venue']
            )
            print(event)
            event.save()
            return event
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def put(data):
        """ Update an event """
        try:
            event = Event.query.get(data['id'])
            if not event:
                abort(400, {'message': 'Invalid event id'})
            data.pop('id')
            for key, value in data.items():
                setattr(event, key, value)
            db.session.commit()
            return event
        except Exception as e:
            print(e)
            return False
