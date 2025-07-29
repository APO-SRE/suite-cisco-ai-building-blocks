from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_entity import IncidentEntity
from ...models.list_incident_entities_response_400 import ListIncidentEntitiesResponse400
from ...models.list_incident_entities_response_401 import ListIncidentEntitiesResponse401
from ...models.list_incident_entities_response_403 import ListIncidentEntitiesResponse403
from ...models.list_incident_entities_response_404 import ListIncidentEntitiesResponse404
from ...models.list_incident_entities_response_500 import ListIncidentEntitiesResponse500
from ...types import Response


def _get_kwargs(
    id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/incident_entities/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        IncidentEntity,
        ListIncidentEntitiesResponse400,
        ListIncidentEntitiesResponse401,
        ListIncidentEntitiesResponse403,
        ListIncidentEntitiesResponse404,
        ListIncidentEntitiesResponse500,
    ]
]:
    if response.status_code == 200:
        response_200 = IncidentEntity.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ListIncidentEntitiesResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ListIncidentEntitiesResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ListIncidentEntitiesResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ListIncidentEntitiesResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ListIncidentEntitiesResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        IncidentEntity,
        ListIncidentEntitiesResponse400,
        ListIncidentEntitiesResponse401,
        ListIncidentEntitiesResponse403,
        ListIncidentEntitiesResponse404,
        ListIncidentEntitiesResponse500,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        IncidentEntity,
        ListIncidentEntitiesResponse400,
        ListIncidentEntitiesResponse401,
        ListIncidentEntitiesResponse403,
        ListIncidentEntitiesResponse404,
        ListIncidentEntitiesResponse500,
    ]
]:
    """List Incident Entities

     Get the detailed entity information for an entity involved in an incident.
    There is a limit of up to 100 ACL's and the data is reflective of the last time we scanned the
    document (not when the incident was created).

    Usage:
    First get an incident/incidents. Then take the id value from the entity
    object within the incident and call the incident_entities endpoint using
    that entitys id (not the incident id).

    Example:
    You have an incident which has an ID of 528815. Lookup the entity id for
    this incident, then use this entity id to get the entity information.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IncidentEntity, ListIncidentEntitiesResponse400, ListIncidentEntitiesResponse401, ListIncidentEntitiesResponse403, ListIncidentEntitiesResponse404, ListIncidentEntitiesResponse500]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        IncidentEntity,
        ListIncidentEntitiesResponse400,
        ListIncidentEntitiesResponse401,
        ListIncidentEntitiesResponse403,
        ListIncidentEntitiesResponse404,
        ListIncidentEntitiesResponse500,
    ]
]:
    """List Incident Entities

     Get the detailed entity information for an entity involved in an incident.
    There is a limit of up to 100 ACL's and the data is reflective of the last time we scanned the
    document (not when the incident was created).

    Usage:
    First get an incident/incidents. Then take the id value from the entity
    object within the incident and call the incident_entities endpoint using
    that entitys id (not the incident id).

    Example:
    You have an incident which has an ID of 528815. Lookup the entity id for
    this incident, then use this entity id to get the entity information.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[IncidentEntity, ListIncidentEntitiesResponse400, ListIncidentEntitiesResponse401, ListIncidentEntitiesResponse403, ListIncidentEntitiesResponse404, ListIncidentEntitiesResponse500]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        IncidentEntity,
        ListIncidentEntitiesResponse400,
        ListIncidentEntitiesResponse401,
        ListIncidentEntitiesResponse403,
        ListIncidentEntitiesResponse404,
        ListIncidentEntitiesResponse500,
    ]
]:
    """List Incident Entities

     Get the detailed entity information for an entity involved in an incident.
    There is a limit of up to 100 ACL's and the data is reflective of the last time we scanned the
    document (not when the incident was created).

    Usage:
    First get an incident/incidents. Then take the id value from the entity
    object within the incident and call the incident_entities endpoint using
    that entitys id (not the incident id).

    Example:
    You have an incident which has an ID of 528815. Lookup the entity id for
    this incident, then use this entity id to get the entity information.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IncidentEntity, ListIncidentEntitiesResponse400, ListIncidentEntitiesResponse401, ListIncidentEntitiesResponse403, ListIncidentEntitiesResponse404, ListIncidentEntitiesResponse500]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        IncidentEntity,
        ListIncidentEntitiesResponse400,
        ListIncidentEntitiesResponse401,
        ListIncidentEntitiesResponse403,
        ListIncidentEntitiesResponse404,
        ListIncidentEntitiesResponse500,
    ]
]:
    """List Incident Entities

     Get the detailed entity information for an entity involved in an incident.
    There is a limit of up to 100 ACL's and the data is reflective of the last time we scanned the
    document (not when the incident was created).

    Usage:
    First get an incident/incidents. Then take the id value from the entity
    object within the incident and call the incident_entities endpoint using
    that entitys id (not the incident id).

    Example:
    You have an incident which has an ID of 528815. Lookup the entity id for
    this incident, then use this entity id to get the entity information.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[IncidentEntity, ListIncidentEntitiesResponse400, ListIncidentEntitiesResponse401, ListIncidentEntitiesResponse403, ListIncidentEntitiesResponse404, ListIncidentEntitiesResponse500]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
